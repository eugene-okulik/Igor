import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject


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
