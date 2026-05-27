import pytest


class TestUpdateObject:
    """Тесты для полного обновления объекта (PUT)."""

    @pytest.mark.critical
    def test_update_existing_object(self, temp_object, update_endpoint):
        """Полное обновление существующего объекта -> данные изменены."""
        object_id = temp_object

        new_payload = {
            "name": "New Name",
            "data": {"title": "New title", "body": "New body"}
        }
        update_endpoint.update_object(object_id, new_payload)

        update_endpoint.check_status_code(200)
        assert update_endpoint.response_json["name"] == "New Name", "Name not updated"
        assert update_endpoint.response_json["data"]["title"] == "New title", "Title not updated"
