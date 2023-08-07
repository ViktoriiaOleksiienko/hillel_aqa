'''Створіть клас з описом будь-якої тварини. Додайте 1 static method, 3 звичайних методи'''


class Penguin:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Color: {self.color}")

    def waddle(self):
        print(f"{self.name} is waddling around")

    def eat_fish(self, amount):
        print(f"{self.name} is eating {amount} fish")

    @staticmethod
    def habitat():
        print("Penguins are commonly found in the Southern Hemisphere")


penguin1 = Penguin("Lolo", 5, "Black and White")

penguin1.display_info()
penguin1.waddle()
penguin1.eat_fish(3)
Penguin.habitat()