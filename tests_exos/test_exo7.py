from exos.exo7 import reverse_tuple_elements


def test_reverse_tuple_elements():
    assert reverse_tuple_elements([(1, 2, 3), (4, 5), (6, 7, 8, 9)]) == [(3, 2, 1), (5, 4), (9, 8, 7, 6)]


def test_reverse_tuple_elements_bis():
    assert reverse_tuple_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)]) == [(3, 2, 1), (6, 5, 4), (9, 8, 7)]


def test_reverse_tuple_elements_ter():
    assert reverse_tuple_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12, 13)]) == [(3, 2, 1), (6, 5, 4), (9, 8, 7), (13, 12, 11, 10)]
