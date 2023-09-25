'''Опишіть класс будь-якого транспортного засобу. Скористайтесь двома рівнями наслідування і абстракцією
за допомогою ABC(використання ABC не рахується за рівень наслідування)'''

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def move(self):
        pass


class Airplane(Transport):
    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed

    def move(self):
        return f"The airplane {self.model} is flying at a speed of {self.max_speed} km/h."


class PassengerAirplane(Airplane):
    def __init__(self, model, max_speed, passenger_capacity):
        super().__init__(model, max_speed)
        self.passenger_capacity = passenger_capacity

    def info(self):
        return f"{self.model} is a passenger airplane with a maximum speed of {self.max_speed} km/h and a passenger capacity of {self.passenger_capacity} passengers."


class MilitaryAirplane(Airplane):
    def __init__(self, model, max_speed, weapon_type):
        super().__init__(model, max_speed)
        self.weapon_type = weapon_type

    def info(self):
        return f"{self.model} is a military airplane with a maximum speed of {self.max_speed} km/h and equipped with {self.weapon_type}."


passenger_plane = PassengerAirplane("Boeing 747", 777, 456)
military_plane = MilitaryAirplane("F-16", 3000, "missiles and cannons")

print(passenger_plane.info())
print(passenger_plane.move())

print(military_plane.info())
print(military_plane.move())