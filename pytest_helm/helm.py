import tempfile
import subprocess
import yaml
import os


class Helm:
    def __init__(self, helm_cmd="helm"):
        self.helm_cmd = helm_cmd

    def run_command(self, *args):
        """
        Runs a command and returns stdout
        """
        result = subprocess.run(args, stdout=subprocess.PIPE)
        if result.returncode != 0:
            raise RuntimeError(f"Error running command {' '.join(args)}")
        return result.stdout

    def helm_template(self, chart, values={}):
        """
        Generates helm templates from a chart
        `values` can be passed to override the default chart values
        """
        fd, path = tempfile.mkstemp()
        output = ""
        try:
            with os.fdopen(fd, 'w') as tmp:
                tmp.write(yaml.dump(values))
            output = self.run_command(
                self.helm_cmd, 'template', chart, '--values', path)
        finally:
            os.remove(path)

        print(output)  # This should only be displayed if the test failed

        return yaml.safe_load_all(output)

    def get_resources(self, manifests, *,
                      api_version=None,
                      kind=None,
                      name=None,
                      predicate=None):
        """
        Get the manifests matching given criteria
        """
        docs = manifests
        if predicate:
            docs = [doc for doc in docs if predicate(doc)]
        if api_version:
            docs = [doc for doc in docs if api_version ==
                    doc.get('apiVersion')]
        if kind:
            docs = [doc for doc in docs if kind == doc.get('kind')]
        if name:
            docs = [doc for doc in docs if name ==
                    doc.get('metadata', {}).get('name')]
        return docs

    def get_resource(self, *args, **kwargs):
        """
        Get one manifest.
        This will raise LookupError if none or more than one manifest is found
        """
        manifests = self.get_resources(*args, **kwargs)
        if len(manifests) != 1:
            raise LookupError(
                "{} manifest found".format(
                    'No' if len(manifests) == 0 else 'More than one'
                ))
        return manifests[0]
