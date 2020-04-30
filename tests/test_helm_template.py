import pytest
# from pytest_helm import helm_template
from unittest.mock import patch


@pytest.mark.skip(reason="Work in progress")
@patch('pytest_helm.run_command')
def test_helm_template(mocked_run_command):
    # helm_template('my_chart', {'key': 'value'})
    mocked_run_command.assert_called_with(
        'helm', 'template', 'my_chart', '--values', '/tmp/file')
