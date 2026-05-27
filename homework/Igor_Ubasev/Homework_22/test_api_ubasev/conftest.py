import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.patch_object import PatchObject
from endpoints.update_object import UpdateObject


@pytest.fixture
def create_endpoint():
    """Фикстура возвращает экземпляр CreateObject."""
    return CreateObject()


@pytest.fixture
def patch_endpoint():
    """Фикстура возвращает экземпляр PatchObject."""
    return PatchObject()


@pytest.fixture
def update_endpoint():
    """Фикстура возвращает экземпляр UpdateObject."""
    return UpdateObject()


@pytest.fixture
def delete_endpoint():
    """Фикстура возвращает экземпляр DeleteObject."""
    return DeleteObject()


@pytest.fixture
def get_endpoint():
    """Фикстура возвращает экземпляр GetObject."""
    return GetObject()


@pytest.fixture
def temp_object():
    """Фикстура создаёт объект и возвращает его ID. Объект удаляется после теста."""
    create_endpoint = CreateObject()
    payload = {
        "name": "Test Object",
        "data": {
            "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo",
            "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf"
        }
    }
    create_endpoint.create_object(payload)
    object_id = create_endpoint.get_object_id()
    yield object_id
    # Удаляем объект после теста
    DeleteObject().delete_object(object_id)
