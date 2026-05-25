import pytest
from endpoints.create_object import CreateObject


class TestCreateObject:
    """Тесты для создания объекта."""

    @pytest.mark.critical
    def test_create_object_with_valid_data(self):
        """Создание объекта с валидными данными -> код 200, id присутствует."""
        payload = {
            "name": "Test Object 1",
            "data": {
                "title": "First test object",
                "body": "First body content"
            }
        }
        create = CreateObject()
        response_json = create.create_object(payload)

        create.check_status_code(200)
        assert "id" in response_json, "Response does not contain 'id'"
        assert response_json["name"] == payload["name"], "Name mismatch"

        # Очистка: удаляем созданный объект
        from endpoints.delete_object import DeleteObject
        DeleteObject().delete_object(response_json["id"])
