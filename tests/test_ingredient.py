import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:

    @pytest.mark.parametrize('price', [1000, 100.5, 0])
    def test_get_price_returns_ingredient_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус космос', price)
            
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('name', ['Соус космос', 'Соус Уран', 'Соус кольца Сатурна'])
    def test_get_name_returns_ingredient_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
        
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE])
    def test_get_type_returns_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'Ингредиент', 100)

        assert ingredient.get_type() == ingredient_type