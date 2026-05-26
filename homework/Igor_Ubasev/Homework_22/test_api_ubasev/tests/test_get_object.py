import pytest
from endpoints.get_object import GetObject


class TestGetObject:
    """Тесты для получения объекта по ID."""

    @pytest.mark.medium
    def test_get_existing_object(self, temp_object):
        """Получение существующего объекта -> код 200, данные совпадают."""
        object_id = temp_object

        # Основное действие: получить объект
        get = GetObject()
        get.get_object_by_id(object_id)

        # Проверки
        get.check_status_code(200)
        assert get.response_json["id"] == object_id, "ID mismatch"
        assert "name" in get.response_json, "Name missing"
        assert "data" in get.response_json, "Data missing"
