# -*- coding: utf-8 -*-
import pytest
from .helm import Helm


def pytest_addoption(parser):
    group = parser.getgroup('helm')
    group.addoption(
        '--helm-path',
        action='store',
        dest='helm_path',
        default='helm',
        help='Path to the helm binary.'
    )

    parser.addini('HELM_PATH', 'Path to the helm binary')


def pytest_report_header(config):
    return "helm binary: {}".format(config.getoption("helm_path"))


@pytest.fixture
def helm(request):
    helm_path = request.config.getoption("helm_path")
    return Helm(helm_path)
