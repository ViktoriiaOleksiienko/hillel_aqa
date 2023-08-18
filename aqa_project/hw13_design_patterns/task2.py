'''Опишіть частину функціоналу замовлення в ресторані. OrderPart клас має метод, що повертає певне блюдо.
Можуть бути різні блюда, наприклад Risotto, Pasta, Pizza, які наслідуються від одного батьківського
абстрактного класу Dish(Factory).'''

from abc import ABC, abstractmethod


class DishFactory(ABC):
    @abstractmethod
    def create_dish(self):
        pass


class Risotto(DishFactory):
    def create_dish(self):
        return "Risotto"


class Pasta(DishFactory):
    def create_dish(self):
        return "Pasta"


class Pizza(DishFactory):
    def create_dish(self):
        return "Pizza"


class OrderPart:
    def get_dish(self, dish_factory):
        dish = dish_factory.create_dish()
        print(f"Ordered: {dish}")


order_part = OrderPart()

risotto_factory = Risotto()
pasta_factory = Pasta()
pizza_factory = Pizza()

order_part.get_dish(risotto_factory)
order_part.get_dish(pasta_factory)
order_part.get_dish(pizza_factory)