import pytest
from to_test import Product


@pytest.fixture
def products():
    return Product("milk", 150, 10)


@pytest.mark.parametrize("myinput, myoutput",[(320, 319),(16,15)])
def test_subtract_quantity(products, myinput, myoutput):
    products.quantity = myinput
    products.subtract_quantity()
    assert products.quantity == myoutput


@pytest.mark.parametrize("myinput, myoutput",[(319, 320),(15,16)])
def test_add_quantity(products, myinput, myoutput):
    products.quantity = myinput
    products.add_quantity()
    assert products.quantity == myoutput


@pytest.mark.parametrize("myinput, myoutput",[(320, 320),(16,16),(-22, -22)])
def test_change_price(products, myinput, myoutput):
    products.change_price(myinput)
    assert products.price == myoutput


