import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject


class TestUpdateObject:
    """Тесты для полного обновления объекта (PUT)."""

    @pytest.mark.critical
    def test_update_existing_object(self):
        """Полное обновление существующего объекта -> данные изменены."""
        # Предусловие: создать объект
        create = CreateObject()
        payload = {
            "name": "Old Name",
            "data": {"title": "Old title", "body": "Old body"}
        }
        create.create_object(payload)
        object_id = create.get_object_id()

        # Обновление
        new_payload = {
            "name": "New Name",
            "data": {"title": "New title", "body": "New body"}
        }
        update = UpdateObject()
        update.update_object(object_id, new_payload)

        update.check_status_code(200)
        assert update.response_json["name"] == "New Name", "Name not updated"
        assert update.response_json["data"]["title"] == "New title", "Title not updated"

        # Очистка
        DeleteObject().delete_object(object_id)
