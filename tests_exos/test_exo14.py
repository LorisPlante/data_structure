from exos.exo14 import out_of_stock_products
def test_out_of_stock_products():
    products = {
        1: {'price': 100, 'quantity': 0},
        2: {'price': 200, 'quantity': 0},
        3: {'price': 300, 'quantity': 0},
        4: {'price': 400, 'quantity': 0},
    }
    expected = [
        (1, 100),
        (2, 200),
        (3, 300),
        (4, 400),
    ]
    assert out_of_stock_products(products) == expected