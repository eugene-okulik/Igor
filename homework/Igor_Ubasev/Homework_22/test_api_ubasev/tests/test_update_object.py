import pytest
from endpoints.update_object import UpdateObject


class TestUpdateObject:
    """Тесты для полного обновления объекта (PUT)."""

    @pytest.mark.critical
    def test_update_existing_object(self, temp_object):
        """Полное обновление существующего объекта -> данные изменены."""
        object_id = temp_object

        new_payload = {
            "name": "New Name",
            "data": {"title": "New title", "body": "New body"}
        }
        update = UpdateObject()
        update.update_object(object_id, new_payload)

        update.check_status_code(200)
        assert update.response_json["name"] == "New Name", "Name not updated"
        assert update.response_json["data"]["title"] == "New title", "Title not updated"
