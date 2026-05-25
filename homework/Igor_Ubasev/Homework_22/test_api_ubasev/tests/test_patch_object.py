import pytest
from endpoints.create_object import CreateObject
from endpoints.patch_object import PatchObject
from endpoints.delete_object import DeleteObject


class TestPatchObject:
    """Тесты для частичного обновления объекта (PATCH)."""

    @pytest.mark.critical
    def test_patch_object_data_field(self):
        """Частичное обновление поля data -> изменяется только указанное поле."""
        # Предусловие: создать объект
        create = CreateObject()
        payload = {
            "name": "Original",
            "data": {"title": "Original title", "body": "Original body"}
        }
        create.create_object(payload)
        object_id = create.get_object_id()

        # Частичное обновление
        patch_payload = {"data": {"title": "Patched title"}}
        patch = PatchObject()
        patch.patch_object(object_id, patch_payload)

        patch.check_status_code(200)
        assert patch.response_json["data"]["title"] == "Patched title", "Title not patched"
        # Остальные поля не должны измениться (проверяем имя)
        assert patch.response_json["name"] == "Original", "Name should not change"

        # Очистка
        DeleteObject().delete_object(object_id)
