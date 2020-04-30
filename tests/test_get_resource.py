import pytest


@pytest.fixture
def manifests():
    return [
        {
            'apiVersion': 'test/v1alpha1',
            'kind': 'kind1',
            'metadata': {
                'name': 'test1',
            },
            'id': 1,
        },
        {
            'apiVersion': 'test/v1',
            'kind': 'kind1',
            'metadata': {
                'name': 'test2',
            },
            'id': 2,
        },
        {
            'apiVersion': 'test/v1',
            'kind': 'kind2',
            'metadata': {
                'name': 'test1',
            },
            'id': 3,
        },
    ]


def test_get_resources_by_api_version(helm, manifests):
    resources = helm.get_resources(manifests, api_version='test/v1')
    assert len(resources) == 2
    assert resources[0]['id'] == 2
    assert resources[1]['id'] == 3


def test_get_resources_by_kind(helm, manifests):
    resources = helm.get_resources(manifests, kind='kind1')
    assert len(resources) == 2
    assert resources[0]['id'] == 1
    assert resources[1]['id'] == 2


def test_get_resources_by_name(helm, manifests):
    resources = helm.get_resources(manifests, name='test1')
    assert len(resources) == 2
    assert resources[0]['id'] == 1
    assert resources[1]['id'] == 3


def test_get_resources_by_predicate(helm, manifests):
    resources = helm.get_resources(
        manifests, predicate=lambda doc: doc['id'] == 2)
    assert len(resources) == 1
    assert resources[0]['id'] == 2


def test_get_resources(helm, manifests):
    resources = helm.get_resources(manifests, kind='kind1')
    assert len(resources) == 2


def test_get_resource(helm, manifests):
    resource = helm.get_resource(manifests, kind='kind1', name='test2')
    assert resource['kind'] == 'kind1'
    assert resource['metadata']['name'] == 'test2'
    assert resource['id'] == 2


def test_get_resource_not_found(helm, manifests):
    with pytest.raises(LookupError) as e:
        helm.get_resource(manifests, kind='kind1', name='notfound')
    assert "No manifest found" in str(e)


def test_get_resource_multiple_found(helm, manifests):
    with pytest.raises(LookupError) as e:
        helm.get_resource(manifests, kind='kind1')
    assert "More than one manifest found" in str(e)
