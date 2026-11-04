import pytest
from unittest.mock import Mock
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_set_buns_sets_burger_bun(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        burger.set_buns(mock_bun)

        assert burger.bun is mock_bun

    def test_add_ingredient_appends_ingredient_to_list(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]

    @pytest.mark.parametrize('index, remaining', [
        (0, (1, 2)),
        (1, (0, 2)),
        (2, (0, 1)),
    ])
    def test_remove_ingredient_deletes_ingredient_from_list(self, index, remaining):
        burger = Burger()
        ingredients = [Mock(spec=Ingredient), Mock(spec=Ingredient), Mock(spec=Ingredient)]
        burger.ingredients = list(ingredients)

        burger.remove_ingredient(index)

        assert burger.ingredients == [ingredients[i] for i in remaining]

    @pytest.mark.parametrize('index, new_index, expected', [
        (0, 1, (1, 0, 2)),
        (1, 2, (0, 2, 1)),
        (2, 0, (2, 0, 1)),
    ])
    def test_move_ingredient_moves_ingredient_to_new_position(self, index, new_index, expected):
        burger = Burger()
        ingredients = [Mock(spec=Ingredient), Mock(spec=Ingredient), Mock(spec=Ingredient)]
        burger.ingredients = list(ingredients)

        burger.move_ingredient(index, new_index)

        assert burger.ingredients == [ingredients[i] for i in expected]

    @pytest.mark.parametrize('bun_price, ingredient_prices, expected', [
        (100, [], 200),
        (100, [50], 250),
        (100, [50, 150], 400),
    ])
    def test_get_price_returns_total_price(self, bun_price, ingredient_prices, expected):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected

    @pytest.mark.parametrize('ingredient_type, expected_type', [
        (INGREDIENT_TYPE_FILLING, 'filling'),
        (INGREDIENT_TYPE_SAUCE, 'sauce')
    ])
    def test_get_receipt_returns_string_receipt(self, ingredient_type, expected_type):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_ingredient = Mock(spec=Ingredient)

        mock_bun.get_name.return_value = 'black bun'
        mock_bun.get_price.return_value = 100
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = 'hot sauce'
        mock_ingredient.get_price.return_value = 100

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_string = f'(==== black bun ====)\n= {expected_type} hot sauce =\n(==== black bun ====)\n\nPrice: 300'

        assert burger.get_receipt() == expected_string


    