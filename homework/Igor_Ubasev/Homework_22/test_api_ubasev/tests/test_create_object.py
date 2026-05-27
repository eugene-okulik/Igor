import pytest


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
        create_endpoint.check_has_id()
        create_endpoint.check_name_matches(payload["name"])

        # Очистка: удаляем созданный объект
        delete_endpoint.delete_object(response_json["id"])
