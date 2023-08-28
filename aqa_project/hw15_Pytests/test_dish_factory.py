import pytest
from hw15_Pytests.dishes import DishFactory, Risotto, Pasta, Pizza, OrderPart


class TestDishFactory:
    @pytest.fixture
    def order_part(self):
        return OrderPart()

    @pytest.mark.smoke
    @pytest.mark.parametrize("dish_factory", [Risotto(), Pasta(), Pizza()])
    def test_create_dish(self, dish_factory, order_part):
        order_part.get_dish(dish_factory)

    @pytest.mark.regression
    def test_invalid_dish_factory(self, order_part):
        class InvalidDishFactory(DishFactory):
            pass

        with pytest.raises(TypeError):
            order_part.get_dish(InvalidDishFactory())

    @pytest.mark.regression
    def test_invalid_dish_creation(self, order_part):
        class InvalidDish(DishFactory):
            def create_dish(self):
                return 123  # not a valid dish

        invalid_dish_factory = InvalidDish()
        result = order_part.get_dish(invalid_dish_factory)
        assert result is None
