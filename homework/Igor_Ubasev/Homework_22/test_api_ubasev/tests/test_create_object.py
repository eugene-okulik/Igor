import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject


@pytest.fixture
def create_endpoint():
    """Фикстура возвращает экземпляр CreateObject."""
    return CreateObject()


@pytest.fixture
def delete_endpoint():
    """Фикстура возвращает экземпляр DeleteObject."""
    return DeleteObject()


class TestCreateObject:
    """Тесты для создания объекта."""

    @pytest.mark.critical
    def test_create_object_with_valid_data(self, create_endpoint, delete_endpoint):
        """Создание объекта с валидными данными -> код 200, id присутствует."""
        payload = {
            "name": "Test Object 1",
            "data": {
                "title": "First test object",
                "body": "First body content"
            }
        }
        response_json = create_endpoint.create_object(payload)

        create_endpoint.check_status_code(200)
        assert "id" in response_json, "Response does not contain 'id'"
        assert response_json["name"] == payload["name"], "Name mismatch"

        # Очистка: удаляем созданный объект
        delete_endpoint.delete_object(response_json["id"])
