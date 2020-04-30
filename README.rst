===========
pytest-helm
===========

.. image:: https://img.shields.io/pypi/v/pytest-helm.svg
    :target: https://pypi.org/project/pytest-helm
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-helm.svg
    :target: https://pypi.org/project/pytest-helm
    :alt: Python versions

.. image:: https://travis-ci.org/nilscan/pytest-helm.svg?branch=master
    :target: https://travis-ci.org/nilscan/pytest-helm
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/nilscan/pytest-helm?branch=master
    :target: https://ci.appveyor.com/project/nilscan/pytest-helm/branch/master
    :alt: See Build Status on AppVeyor

Pytest helpers to test Helm charts

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------

* Render helm templates and make assertion on generated resources
* Helpers to load resources by GVK and name


Requirements
------------

* Python >= 3.8
* PyTest >= 5.4


Installation
------------

You can install "pytest_helm" via `pip`_ from `PyPI`_::

    $ pip install pytest_helm


Usage
-----

* `helm`_ fixture

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-helm" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/nilscan/pytest-helm/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
