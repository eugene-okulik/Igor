import requests

BASE_URL = "http://objapi.course.qa-practice.com"


def post_an_object():
    """POST /object - создание нового объекта"""
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
    assert response.status_code == 200, "Status code is incorrect"
    assert "id" in response.json(), "Id is missing in response"


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
    requests.delete(f"{BASE_URL}/object/{object_id}")


def put_an_object():
    """PUT /object/<id> - полное обновление объекта"""
    object_id = new_object()
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
    clear(object_id)


def patch_object_data():
    """PATCH /object/<id> - частичное обновление только data"""
    object_id = new_object()
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
    clear(object_id)


def delete_an_object():
    """DELETE /object/<id> - удаление объекта"""
    object_id = new_object()
    response = requests.delete(f"{BASE_URL}/object/{object_id}")
    assert response.status_code == 200, "Status code is incorrect"
