import pytest
import requests
import warnings

# Отключаем только конкретные предупреждения, остальные оставляем
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=ResourceWarning)

BASE_URL = "http://objapi.course.qa-practice.com"


def new_object():
    """Вспомогательная функция - создание объекта и возврат его id."""
    body = {
        "name": "Test Object",
        "data": {
            "title": (
                "fsakjdhfkasjdhflkajsdhlkfjashdfoo"
            ),
            "body": (
                "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf"
            ),
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        f"{BASE_URL}/object",
        json=body,
        headers=headers,
    )
    return response.json()["id"]


def clear(object_id):
    """Вспомогательная функция - удаление объекта."""
    try:
        requests.delete(f"{BASE_URL}/object/{object_id}")
    except Exception:
        pass


@pytest.fixture(scope="session", autouse=True)
def session_scope():
    """Фикстура для действий до и после всех тестов."""
    print("\n" + "=" * 50)
    print("Start testing")
    print("=" * 50)
    yield
    print("\n" + "=" * 50)
    print("Testing completed")
    print("=" * 50)


@pytest.fixture(scope="function", autouse=True)
def test_lifecycle():
    """Фикстура для вывода сообщений до и после каждого теста."""
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture
def object_for_update():
    """Создаёт объект для PUT-теста, после теста удаляет."""
    object_id = new_object()
    print(f"\n[DEBUG] Created object for PUT: {object_id}")
    yield object_id
    clear(object_id)
    print(f"[DEBUG] Cleaned up object for PUT: {object_id}")


@pytest.fixture
def object_for_get():
    """Создаёт объект для GET-теста, после теста удаляет."""
    object_id = new_object()
    print(f"\n[DEBUG] Created object for GET: {object_id}")
    yield object_id
    clear(object_id)
    print(f"[DEBUG] Cleaned up object for GET: {object_id}")


@pytest.fixture
def object_for_patch():
    """Создаёт объект для PATCH-теста, после теста удаляет."""
    object_id = new_object()
    print(f"\n[DEBUG] Created object for PATCH: {object_id}")
    yield object_id
    clear(object_id)
    print(f"[DEBUG] Cleaned up object for PATCH: {object_id}")


@pytest.fixture
def object_for_delete():
    """Создаёт объект для DELETE-теста (удаление происходит в тесте)."""
    object_id = new_object()
    print(f"\n[DEBUG] Created object for DELETE: {object_id}")
    yield object_id
    # Если тест упал, объект мог не удалиться – почистим
    clear(object_id)
    print(f"[DEBUG] Cleaned up object for DELETE: {object_id}")


@pytest.mark.critical
@pytest.mark.parametrize(
    "test_data",
    [
        {
            "name": "Test Object 1",
            "data": {
                "title": "First test object",
                "body": "First body content",
            },
        },
        {
            "name": "Test Object 2",
            "data": {
                "title": "Second test object",
                "body": "Second body content",
            },
        },
        {
            "name": "Test Object 3",
            "data": {
                "title": "Third test object",
                "body": "Third body content",
            },
        },
    ],
)
def test_create_object(test_data):
    """Тест создания объекта с разными данными."""
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        f"{BASE_URL}/object",
        json=test_data,
        headers=headers,
    )
    assert response.status_code == 200, (
        f"Status code error: {response.status_code}"
    )
    assert "id" in response.json(), "Id is missing in response"
    assert response.json()["name"] == test_data["name"], "Name mismatch"

    # Очистка
    object_id = response.json()["id"]
    clear(object_id)


@pytest.mark.critical
def test_update_object(object_for_update):
    """Тест полного обновления объекта (PUT)."""
    object_id = object_for_update

    body = {
        "name": "Updated Object PUT",
        "data": {
            "title": (
                "fsakjdhfkasjdhflkajsdhlkfjashdfoo-UPD"
            ),
            "body": (
                "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf-UPD"
            ),
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"{BASE_URL}/object/{object_id}",
        json=body,
        headers=headers,
    ).json()

    assert response["name"] == "Updated Object PUT", "Name was not updated"
    assert (
        response["data"]["title"]
        == "fsakjdhfkasjdhflkajsdhlkfjashdfoo-UPD"
    ), "Title was not updated"
    print(f"[DEBUG] PUT test passed for object {object_id}")


@pytest.mark.medium
def test_get_object_by_id(object_for_get):
    """Тест получения объекта по ID."""
    object_id = object_for_get

    response = requests.get(f"{BASE_URL}/object/{object_id}")

    assert response.status_code == 200, (
        f"Status code error: {response.status_code}"
    )
    assert response.json()["id"] == object_id, "Object ID mismatch"
    assert "name" in response.json(), "Name is missing"
    assert "data" in response.json(), "Data is missing"
    print(f"[DEBUG] GET test passed for object {object_id}")


@pytest.mark.critical
def test_patch_object(object_for_patch):
    """Тест частичного обновления объекта (PATCH)."""
    object_id = object_for_patch

    body = {
        "data": {
            "title": "Patched Title Only",
            "body": "Patched body content",
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"{BASE_URL}/object/{object_id}",
        json=body,
        headers=headers,
    ).json()

    assert response["data"]["title"] == "Patched Title Only", (
        "Data was not patched"
    )
    print(f"[DEBUG] PATCH test passed for object {object_id}")


@pytest.mark.medium
def test_delete_object(object_for_delete):
    """Тест удаления объекта."""
    object_id = object_for_delete

    response = requests.delete(f"{BASE_URL}/object/{object_id}")
    assert response.status_code == 200, (
        f"Status code error: {response.status_code}"
    )
    print(f"[DEBUG] Object {object_id} deleted")

    # Проверка: объект действительно удалён
    get_response = requests.get(f"{BASE_URL}/object/{object_id}")
    assert get_response.status_code == 404, (
        "Object still exists after deletion"
    )
    print(f"[DEBUG] DELETE test passed for object {object_id}")
