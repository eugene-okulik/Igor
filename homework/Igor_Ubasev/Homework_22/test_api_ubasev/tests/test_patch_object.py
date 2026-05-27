import pytest


class TestPatchObject:
    """Тесты для частичного обновления объекта (PATCH)."""

    @pytest.mark.critical
    def test_patch_object_data_field(self, temp_object, patch_endpoint):
        """Частичное обновление поля data -> изменяется только указанное поле."""
        object_id = temp_object

        patch_payload = {"data": {"title": "Patched title"}}
        patch_endpoint.patch_object(object_id, patch_payload)

        patch_endpoint.check_status_code(200)
        assert patch_endpoint.response_json["data"]["title"] == "Patched title"
        # Имя не должно измениться (исходное имя "Test Object" из фикстуры)
        assert patch_endpoint.response_json["name"] == "Test Object"
