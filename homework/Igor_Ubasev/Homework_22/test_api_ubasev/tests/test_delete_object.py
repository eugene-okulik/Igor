import pytest


class TestDeleteObject:
    """Тесты для удаления объекта."""

    @pytest.mark.medium
    def test_delete_existing_object(self, temp_object, delete_endpoint, get_endpoint):
        """
        Удаление существующего объекта -> код 200, при повторном GET - 404.
        """
        object_id = temp_object

        # Шаг 1: удалить объект
        delete_endpoint.delete_object(object_id)
        delete_endpoint.check_status_code(200)

        # Шаг 2: убедиться, что объект больше не существует
        get_endpoint.get_object_by_id(object_id)
        get_endpoint.check_status_code(404)
