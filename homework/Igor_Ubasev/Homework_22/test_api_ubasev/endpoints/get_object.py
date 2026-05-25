import requests
from endpoints.base_endpoint import BaseEndpoint
from config import BASE_URL


class GetObject(BaseEndpoint):
    """Класс для получения объекта по ID (GET /object/{id})."""

    def get_object_by_id(self, object_id):
        """Отправляет GET запрос для получения объекта."""
        self.response = requests.get(f"{BASE_URL}/object/{object_id}")
        if self.response.status_code == 200:
            self.response_json = self.response.json()
        return self.response
