from exos.exo16 import symmetric_difference


def test_symmetric_difference():
    assert symmetric_difference({1, 2, 3}, {2, 3, 4}) == {1, 4}


def test_symmetric_difference_bis():
    assert symmetric_difference({1, 2, 3, 5}, {2, 3, 4, 6}) == {1, 4, 5, 6}


def test_symmetric_difference_ter():
    assert symmetric_difference({1, 2, 3}, {2, 4, 5}) == {1, 4, 3, 5}
