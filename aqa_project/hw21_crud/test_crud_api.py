import hw21_crud.infrastructure as infra


def test_get_object():
    assert infra.get_an_object(4).status_code == 200


#with 404 - invalid url
def test_get_object_with_invalid_url():
    response = infra.get_an_object("https://www.google.com/")
    assert response.status_code == 404
    assert "error" in response.json()
    print(response.json())


def test_create_an_object():
    response, obj_id = infra.create_an_object()
    get_response = infra.get_an_object(obj_id)
    assert response.status_code == 200
    assert get_response.status_code == 200
    print(get_response.json())


#not 201
def test_create_object_with_different_status_code():
    response, obj_id = infra.create_an_object()
    assert response.status_code != 201
    print("Status Code:", response.status_code)
    print(response.json())


def test_update_object():
    response, obj_id = infra.create_an_object()
    changed_obj = infra.update_an_object(obj_id, {"name": "name is no more Apple", "data": {"color": "white", "generation": "3rd", "price": 135}})
    assert response.status_code == 200
    assert changed_obj.status_code == 200
    print(changed_obj.json())


#code 200
def test_update_object_with_valid_data():
    response, obj_id = infra.create_an_object()
    updated_data = {"name": "Updated Name", "data": {"color": "black"}}
    response = infra.update_an_object(obj_id, updated_data)
    assert response.status_code == 200
    get_response = infra.get_an_object(obj_id)
    assert get_response.status_code == 200
    assert get_response.json()["name"] == updated_data["name"]
    assert get_response.json()["data"]["color"] == updated_data["data"]["color"]


def test_delete_object():
    response, obj_id = infra.create_an_object()
    deleted_obj = infra.delete_an_object(obj_id)
    assert deleted_obj.status_code == 200
    print(deleted_obj.json())


#nonexistent_object
def test_delete_nonexistent_object():
    response = infra.delete_an_object(9999)
    assert response.status_code == 404
    assert "error" in response.json()

