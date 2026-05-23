import pytest
import requests

BASE_URL = "http://objapi.course.qa-practice.com"


def new_object():
    """Вспомогательная функция - создание объекта и возврат его id."""
    body = {
        "name": "Test Object",
        "data": {
            "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo",
            "body": (
                "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf"
            ),
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        f"{BASE_URL}/object", json=body, headers=headers
    )
    return response.json()["id"]


def clear(object_id):
    """Удаляет объект, если он существует."""
    try:
        # Сначала проверяем, существует ли объект
        check = requests.get(f"{BASE_URL}/object/{object_id}")
        if check.status_code == 200:
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
def temp_object():
    """Создаёт временный объект, после теста удаляет (если ещё существует)."""
    object_id = new_object()
    print(f"\n[DEBUG] Created temporary object: {object_id}")
    yield object_id
    clear(object_id)
    print(f"[DEBUG] Cleaned up temporary object: {object_id}")


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
        f"{BASE_URL}/object", json=test_data, headers=headers
    )
    assert response.status_code == 200, (
        f"Status code error: {response.status_code}"
    )
    assert "id" in response.json(), "Id is missing in response"
    assert response.json()["name"] == test_data["name"], "Name mismatch"

    object_id = response.json()["id"]
    clear(object_id)  # удаляем созданный в тесте объект


@pytest.mark.critical
def test_update_object(temp_object):
    """Тест полного обновления объекта (PUT)."""
    object_id = temp_object

    body = {
        "name": "Updated Object PUT",
        "data": {
            "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo-UPD",
            "body": (
                "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf-UPD"
            ),
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"{BASE_URL}/object/{object_id}", json=body, headers=headers
    ).json()

    assert response["name"] == "Updated Object PUT", "Name was not updated"
    assert (
        response["data"]["title"]
        == "fsakjdhfkasjdhflkajsdhlkfjashdfoo-UPD"
    ), "Title was not updated"
    print(f"[DEBUG] PUT test passed for object {object_id}")


@pytest.mark.medium
def test_get_object_by_id(temp_object):
    """Тест получения объекта по ID."""
    object_id = temp_object

    response = requests.get(f"{BASE_URL}/object/{object_id}")

    assert response.status_code == 200, (
        f"Status code error: {response.status_code}"
    )
    assert response.json()["id"] == object_id, "Object ID mismatch"
    assert "name" in response.json(), "Name is missing"
    assert "data" in response.json(), "Data is missing"
    print(f"[DEBUG] GET test passed for object {object_id}")


@pytest.mark.critical
def test_patch_object(temp_object):
    """Тест частичного обновления объекта (PATCH)."""
    object_id = temp_object

    body = {
        "data": {
            "title": "Patched Title Only",
            "body": "Patched body content",
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"{BASE_URL}/object/{object_id}", json=body, headers=headers
    ).json()

    assert response["data"]["title"] == "Patched Title Only", (
        "Data was not patched"
    )
    print(f"[DEBUG] PATCH test passed for object {object_id}")


@pytest.mark.medium
def test_delete_object(temp_object):
    """Тест удаления объекта."""
    object_id = temp_object

    response = requests.delete(f"{BASE_URL}/object/{object_id}")
    assert response.status_code == 200, (
        f"Status code error: {response.status_code}"
    )
    print(f"[DEBUG] Object {object_id} deleted")

    get_response = requests.get(f"{BASE_URL}/object/{object_id}")
    assert get_response.status_code == 404, (
        "Object still exists after deletion"
    )
    print(f"[DEBUG] DELETE test passed for object {object_id}")
