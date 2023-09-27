from requests import get, Response
from hw20_api import config


class PeopleService:
    def __init__(self):
        self.__people_url = f"{config['host']}/people"

    def get_people(self, people_id:str) -> Response:
        return get(f"{self.__people_url}/{people_id}")


class Vehicle:
    def __init__(self, name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed
        self.crew = crew
        self.passengers = passengers


class VehicleService:
    def __init__(self):
        self.__vehicles_url = f"{config['host']}/vehicles"

    def get_vehicle(self, vehicle_id: str) -> Response:
        return get(f"{self.__vehicles_url}/{vehicle_id}")

    def get_vehicles(self, page: int = 1) -> Response:
        params = {"page": page}
        return get(self.__vehicles_url, params=params)
