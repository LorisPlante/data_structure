from exos.exo10 import max_of_three_numbers

def test_max_of_three_numbers_four():
    assert max_of_three_numbers(1, 3, 4) == 4

def test_max_of_three_numbers_height():
    assert max_of_three_numbers(3, 5, 8) == 8

def test_max_of_three_numbers_nine():
    assert max_of_three_numbers(9, 2, 6) == 9