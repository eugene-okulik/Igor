import requests
from endpoints.base_endpoint import BaseEndpoint
from config import BASE_URL


class PatchObject(BaseEndpoint):
    """Класс для частичного обновления объекта (PATCH /object/{id})."""

    def patch_object(self, object_id, payload):
        """Отправляет PATCH запрос для частичного обновления."""
        headers = {"Content-Type": "application/json"}
        self.response = requests.patch(
            f"{BASE_URL}/object/{object_id}", json=payload, headers=headers
        )
        self.response_json = self.response.json()
        return self.response_json
