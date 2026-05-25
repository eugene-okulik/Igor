import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject


class TestDeleteObject:
    """Тесты для удаления объекта."""

    @pytest.mark.medium
    def test_delete_existing_object(self):
        """Удаление существующего объекта -> код 200, при повторном GET - 404."""
        # Предусловие: создать объект
        create = CreateObject()
        payload = {
            "name": "To Be Deleted",
            "data": {"title": "Delete me", "body": "body"}
        }
        create.create_object(payload)
        object_id = create.get_object_id()

        # Удаление
        delete = DeleteObject()
        delete.delete_object(object_id)
        delete.check_status_code(200)

        # Проверка, что объект действительно удалён
        get = GetObject()
        get.get_object_by_id(object_id)
        get.check_status_code(404)
