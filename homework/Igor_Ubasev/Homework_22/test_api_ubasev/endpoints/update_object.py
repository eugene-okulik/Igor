import requests
from endpoints.base_endpoint import BaseEndpoint
from config import BASE_URL


class UpdateObject(BaseEndpoint):
    """Класс для полного обновления объекта (PUT /object/{id})."""

    def update_object(self, object_id, payload):
        """Отправляет PUT запрос для обновления объекта."""
        headers = {"Content-Type": "application/json"}
        self.response = requests.put(
            f"{BASE_URL}/object/{object_id}", json=payload, headers=headers
        )
        self.response_json = self.response.json()
        return self.response_json
