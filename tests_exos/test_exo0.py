import pytest
from exos.exo0 import Calculate

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3),
                                            (-1, -2, -3),
                                            (10.5, 10.5, 21)])
def test_addition_with_parametrize(a, b, expected):
    calc = Calculate(a, b)
    assert calc.add() == expected

@pytest.mark.parametrize("a, b, expected", [(1, 2, -1),
                                            (-1, -2, 1),
                                            (10.5, 10.5, 0)])
def test_subtraction_with_parametrize(a, b, expected):
    calc = Calculate(a, b)
    assert calc.subtract() == expected

@pytest.mark.parametrize("a, b, expected", [(1, 2, 2),
                                            (2.5, 4, 10),
                                            (10.5, 10.5, 110.25)])
def test_multiplication_with_parametrize(a, b, expected):
    calc = Calculate(a, b)
    assert calc.multiply() == expected

@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5),
                                            (2.5, 4, 0.625),
                                            (10.5, 10.5, 1)])
def test_division_with_parametrize(a, b, expected):
    calc = Calculate(a, b)
    assert calc.divide() == expected