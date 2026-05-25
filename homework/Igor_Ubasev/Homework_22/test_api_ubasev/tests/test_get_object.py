import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.delete_object import DeleteObject


class TestGetObject:
    """Тесты для получения объекта по ID."""

    @pytest.mark.medium
    def test_get_existing_object(self):
        """Получение существующего объекта -> код 200, данные совпадают."""
        # Предусловие: создать объект
        create = CreateObject()
        payload = {
            "name": "Object for GET",
            "data": {"title": "GET test", "body": "GET body"}
        }
        create.create_object(payload)
        object_id = create.get_object_id()

        # Основное действие: получить объект
        get = GetObject()
        get.get_object_by_id(object_id)

        # Проверки
        get.check_status_code(200)
        assert get.response_json["id"] == object_id, "ID mismatch"
        assert "name" in get.response_json, "Name missing"
        assert "data" in get.response_json, "Data missing"

        # Очистка
        DeleteObject().delete_object(object_id)
