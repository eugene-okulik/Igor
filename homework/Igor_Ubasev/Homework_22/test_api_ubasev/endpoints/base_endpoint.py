import requests


class BaseEndpoint:
    """Базовый класс для всех эндпоинтов."""

    def __init__(self):
        self.response = None
        self.response_json = None

    def check_status_code(self, expected_code):
        """Проверяет, что статус код ответа совпадает с ожидаемым."""
        assert self.response.status_code == expected_code, (
            f"Expected status {expected_code}, got {self.response.status_code}"
        )

    def check_response_field(self, field_name, expected_value):
        """Проверяет, что поле в ответе равно ожидаемому значению."""
        actual_value = self.response_json.get(field_name)
        assert actual_value == expected_value, (
            f"Field '{field_name}': expected {expected_value}, got {actual_value}"
        )
