import pytest


class TestGetObject:
    """Тесты для получения объекта по ID."""

    @pytest.mark.medium
    def test_get_existing_object(self, temp_object, get_endpoint):
        """Получение существующего объекта -> код 200, данные совпадают."""
        object_id = temp_object

        get_endpoint.get_object_by_id(object_id)

        get_endpoint.check_status_code(200)
        assert get_endpoint.response_json["id"] == object_id, "ID mismatch"
        assert "name" in get_endpoint.response_json, "Name missing"
        assert "data" in get_endpoint.response_json, "Data missing"
