# -*- coding: utf-8 -*-


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'helm:',
        '*--helm-path=HELM_PATH*',
    ])


def test_helm_path_ini_setting(testdir):
    testdir.makeini("""
        [pytest]
        HELM_PATH=/path/to/helm
    """)

    testdir.makepyfile("""
        import pytest

        @pytest.fixture
        def helm_path_ini(request):
            return request.config.getini('HELM_PATH')

        def test_helm_path_ini(helm_path_ini):
            assert helm_path_ini == '/path/to/helm'
    """)

    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_helm_path_ini PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
