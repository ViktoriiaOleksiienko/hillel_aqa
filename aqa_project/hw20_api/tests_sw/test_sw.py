from hw20_api.infrastructure.people import People


def test_test_luke(people_service):
    response = people_service.get_people("1")
    assert response.json()['name'] == 'Luke Skywalker'


def test_luke_with_fixture(people_service, first_people1):
    response = people_service.get_people("1")
    actual_people = People(
        **response.json()
    )
    assert actual_people == first_people1


def test_get_vehicle(vehicle_service):
    response = vehicle_service.get_vehicle("4")
    assert response.status_code == 200
    vehicle_data = response.json()
    assert vehicle_data["name"] == "Sand Crawler"


def test_get_vehicles(vehicle_service):
    response = vehicle_service.get_vehicles()
    assert response.status_code == 200
    vehicles_data = response.json()
    assert len(vehicles_data["results"]) > 0


def test_get_next_page_vehicles(vehicle_service):
    response = vehicle_service.get_vehicles(2)
    assert response.status_code == 200
    vehicles_data = response.json()
    assert len(vehicles_data["results"]) > 0
