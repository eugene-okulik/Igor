import pytest
import endpoints.create_object


@pytest.fixture
def temp_object():
    """Фикстура создаёт объект и возвращает его ID. Объект удаляется после теста."""
    create_endpoint = endpoints.CreateObject()
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
    # Удаляем объект после теста, если он ещё существует
    from endpoints.delete_object import DeleteObject
    DeleteObject().delete_object(object_id)
