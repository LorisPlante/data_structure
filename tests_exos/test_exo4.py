from exos.exo4 import FilterList


def test_giveMeaList():
    data = [1, 2, 3, 4, 5, 1, 2, 30, 45, 5, 1, 2, 30, 2, 3, 4]
    assert FilterList.giveMeaList(data) == [1, 2, 3, 4, 5, 30]


def test_giveMeaList_empty():
    data = []
    assert FilterList.giveMeaList(data) == []


def test_giveMeaList_single():
    data = [1]
    assert FilterList.giveMeaList(data) == [1]


def test_giveMeaList_negativ():
    data = [-1, -2, -3, -4, -5, -1, -2, -30, -45, -5, -1, -2, -30, -2, -3, -4]
    assert FilterList.giveMeaList(data) == [-5, -4, -3, -2, -1, -30, -45]


def test_giveMeaList_string():
    data = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
    assert FilterList.giveMeaList(data) == ['a', 'b', 'c', 'd', 'e']