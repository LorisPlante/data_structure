from exos.exo5 import RotationList


def test_rotate_right_two_steps():
    assert RotationList.rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_right_three_steps():
    assert RotationList.rotate_right([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]


def test_rotate_right_no_steps():
    assert RotationList.rotate_right([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
