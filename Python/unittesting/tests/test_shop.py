import pytest
from to_test import Shop, Product


@pytest.fixture
def product():
    return Product("milk", 150, 10)


@pytest.fixture
def shop():
    return Shop()


def test_add_product(shop, product):
    shop.add_product(product)
    assert product in shop.products


@pytest.mark.parametrize("title, myoutput", [("cherry", 0), ("ice-cream", 0), ("sugar", 0)])
def test_get_product_index(title, myoutput, shop):
    tmp = Product(title, 14, 87)
    shop.add_product(tmp)
    assert shop._get_product_index(tmp.title) == myoutput


@pytest.mark.parametrize("title, price, quantity, qty_to_sell",
                         [("sugar", 10, 10, 15), ("kitty", 9, 42, 42), ("cactus", 3, 4, 3)])
def test_sell_products(title, price, quantity, shop, qty_to_sell):
    if quantity < qty_to_sell:
        with pytest.raises(ValueError):
            item = Product(title, price, quantity)
            shop.add_product(item)
            shop.sell_product(title, qty_to_sell)
    else:
        if quantity == qty_to_sell:
            shop.sell_product(title, qty_to_sell)
            assert shop._get_product_index(title) is None
        else:
            item = Product(title, price, quantity)
            shop.add_product(item)
            tmp = quantity - qty_to_sell
            shop.products[0].subtract_quantity(qty_to_sell)
            assert shop.products[0].quantity == tmp






