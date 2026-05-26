import pytest
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject


class TestDeleteObject:
    """Тесты для удаления объекта."""

    @pytest.mark.medium
    def test_delete_existing_object(self, temp_object):
        """
        Удаление существующего объекта -> код 200, при повторном GET - 404.
        """
        object_id = temp_object

        # Шаг 1: удалить объект
        delete = DeleteObject()
        delete.delete_object(object_id)
        delete.check_status_code(200)

        # Шаг 2: убедиться, что объект больше не существует
        get = GetObject()
        get.get_object_by_id(object_id)
        get.check_status_code(404)
