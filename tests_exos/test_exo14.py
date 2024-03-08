from exos.exo14 import out_of_stock_products


def test_out_of_stock_products():
    products = {
        1: {'price': 100, 'quantity': 0},
        2: {'price': 300, 'quantity': 0},
        3: {'price': 700, 'quantity': 0},
        4: {'price': 1000, 'quantity': 0},
    }
    expected = [
        (1, 100),
        (2, 300),
        (3, 700),
        (4, 1000),
    ]
    assert out_of_stock_products(products) == expected
