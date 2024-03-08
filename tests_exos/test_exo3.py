from exos.exo3 import sum_two_numbers


def test_sum_two_positiv_numbers():
    assert sum_two_numbers(1, 2) == 3


def test_sum_two_negativ_numbers():
    assert sum_two_numbers(-1, -1) == -2


def test_sum_two_zero_numbers():
    assert sum_two_numbers(0, 0) == 0
