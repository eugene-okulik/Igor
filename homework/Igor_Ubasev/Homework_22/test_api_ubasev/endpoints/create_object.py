import requests
from endpoints.base_endpoint import BaseEndpoint
from config import BASE_URL


class CreateObject(BaseEndpoint):
    """Класс для создания объекта (POST /object)."""

    def create_object(self, payload):
        """Отправляет POST запрос для создания объекта."""
        headers = {"Content-Type": "application/json"}
        self.response = requests.post(
            f"{BASE_URL}/object", json=payload, headers=headers
        )
        self.response_json = self.response.json()
        return self.response_json

    def get_object_id(self):
        """Возвращает id созданного объекта."""
        return self.response_json.get("id")
