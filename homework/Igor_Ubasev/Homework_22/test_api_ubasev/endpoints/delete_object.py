import requests
from endpoints.base_endpoint import BaseEndpoint
from config import BASE_URL


class DeleteObject(BaseEndpoint):
    """Класс для удаления объекта (DELETE /object/{id})."""

    def delete_object(self, object_id):
        """Отправляет DELETE запрос для удаления объекта."""
        self.response = requests.delete(f"{BASE_URL}/object/{object_id}")
        return self.response
