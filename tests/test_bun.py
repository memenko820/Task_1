import pytest
from bun import Bun


class TestBun:

    @pytest.mark.parametrize('name', ['Вулканическая булка', 'Лунная булка', 'Космическая булка'])
    def test_get_name_returns_bun_name(self, name):
        bun = Bun(name, 100)

        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [1000, 100.5, 0])
    def test_get_price_returns_bun_price(self, price):
        bun = Bun('Булочка', price)
    
        assert bun.get_price() == price