from exos.exo15 import intersection


def test_intersection_two_three():
    assert intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_intersection():
    assert intersection({1, 2, 3}, {4, 5, 6}) == set()


def test_intersection_one_two_three():
    assert intersection({1, 2, 3}, {1, 2, 3}) == {1, 2, 3}


def test_no_intersection_bis():
    assert intersection(set(), {1, 2, 3}) == set()
