import pytest
import requests
import warnings

# Отключаем все предупреждения
warnings.filterwarnings("ignore")

BASE_URL = "http://objapi.course.qa-practice.com"


def new_object():
    """Вспомогательная функция - создание объекта и возврат его id"""
    body = {
        "name": "Test Object",
        "data": {
            "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo",
            "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        f"{BASE_URL}/object",
        json=body,
        headers=headers
    )
    return response.json()["id"]


def clear(object_id):
    """Вспомогательная функция - удаление объекта"""
    try:
        requests.delete(f"{BASE_URL}/object/{object_id}")
    except Exception:  # Исправлено: указываем конкретное исключение
        pass


@pytest.fixture(scope="function", autouse=True)
def test_lifecycle():
    """Fixture для вывода сообщений до и после каждого теста"""
    print("\nbefore test")
    yield
    print("\nafter test")


def pytest_sessionstart(session):
    """Выводится перед запуском всех тестов"""
    print("\n" + "=" * 50)
    print("Start testing")
    print("=" * 50)


def pytest_sessionfinish(session, exitstatus):
    """Выводится после завершения всех тестов"""
    print("\n" + "=" * 50)
    print("Testing completed")
    print("=" * 50)


@pytest.mark.critical
@pytest.mark.parametrize("test_data", [
    {
        "name": "Test Object 1",
        "data": {
            "title": "First test object",
            "body": "First body content"
        }
    },
    {
        "name": "Test Object 2",
        "data": {
            "title": "Second test object",
            "body": "Second body content"
        }
    },
    {
        "name": "Test Object 3",
        "data": {
            "title": "Third test object",
            "body": "Third body content"
        }
    }
])
def test_create_object(test_data):
    """Тест создания объекта с разными данными"""
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        f"{BASE_URL}/object",
        json=test_data,
        headers=headers
    )
    assert response.status_code == 200, f"Status code error: {response.status_code}"
    assert "id" in response.json(), "Id is missing in response"
    assert response.json()["name"] == test_data["name"], "Name mismatch"

    # Очистка
    object_id = response.json()["id"]
    clear(object_id)


@pytest.mark.critical
def test_update_object():
    """Тест полного обновления объекта (PUT)"""
    print("\n[DEBUG] Creating object for PUT test")
    object_id = new_object()
    print(f"[DEBUG] Created object with ID: {object_id}")

    try:
        body = {
            "name": "Updated Object PUT",
            "data": {
                "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo-UPD",
                "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf-UPD"
            }
        }
        headers = {"Content-Type": "application/json"}
        response = requests.put(
            f"{BASE_URL}/object/{object_id}",
            json=body,
            headers=headers
        ).json()

        assert response["name"] == "Updated Object PUT", "Name was not updated"
        assert response["data"]["title"] == "fsakjdhfkasjdhflkajsdhlkfjashdfoo-UPD", \
            "Title was not updated"
        print(f"[DEBUG] PUT test passed for object {object_id}")
    finally:
        clear(object_id)
        print(f"[DEBUG] Cleaned up object {object_id}")


@pytest.mark.medium
def test_get_object_by_id():
    """Тест получения объекта по ID"""
    print("\n[DEBUG] Creating object for GET test")
    object_id = new_object()
    print(f"[DEBUG] Created object with ID: {object_id}")

    try:
        response = requests.get(f"{BASE_URL}/object/{object_id}")

        assert response.status_code == 200, f"Status code error: {response.status_code}"
        assert response.json()["id"] == object_id, "Object ID mismatch"
        assert "name" in response.json(), "Name is missing"
        assert "data" in response.json(), "Data is missing"
        print(f"[DEBUG] GET test passed for object {object_id}")
    finally:
        clear(object_id)
        print(f"[DEBUG] Cleaned up object {object_id}")


@pytest.mark.critical
def test_patch_object():
    """Тест частичного обновления объекта (PATCH)"""
    print("\n[DEBUG] Creating object for PATCH test")
    object_id = new_object()
    print(f"[DEBUG] Created object with ID: {object_id}")

    try:
        body = {
            "data": {
                "title": "Patched Title Only",
                "body": "Patched body content"
            }
        }
        headers = {"Content-Type": "application/json"}
        response = requests.patch(
            f"{BASE_URL}/object/{object_id}",
            json=body,
            headers=headers
        ).json()

        assert response["data"]["title"] == "Patched Title Only", \
            "Data was not patched"
        print(f"[DEBUG] PATCH test passed for object {object_id}")
    finally:
        clear(object_id)
        print(f"[DEBUG] Cleaned up object {object_id}")


@pytest.mark.medium
def test_delete_object():
    """Тест удаления объекта"""
    print("\n[DEBUG] Creating object for DELETE test")
    object_id = new_object()
    print(f"[DEBUG] Created object with ID: {object_id}")

    # Выполнение теста: удаление объекта
    response = requests.delete(f"{BASE_URL}/object/{object_id}")
    assert response.status_code == 200, f"Status code error: {response.status_code}"
    print(f"[DEBUG] Object {object_id} deleted")

    # Проверка: объект действительно удален
    get_response = requests.get(f"{BASE_URL}/object/{object_id}")
    assert get_response.status_code == 404, "Object still exists after deletion"
    print(f"[DEBUG] DELETE test passed for object {object_id}")
