# teste de # Écrivez un programme qui trouve l'intersection de deux ensembles.
#
# def intersection(set1, set2):
#     return set1 & set2

from exos.exo15 import intersection

def test_intersection():
    assert intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}
    assert intersection({1, 2, 3}, {4, 5, 6}) == set()
    assert intersection({1, 2, 3}, {1, 2, 3}) == {1, 2, 3}
    assert intersection({1, 2, 3}, {3, 2, 1}) == {1, 2, 3}
    assert intersection(set(), {1, 2, 3}) == set()
    assert intersection({1, 2, 3}, set()) == set()
    assert intersection(set(), set()) == set()
    assert intersection({1, 2, 3}, {3, 2, 1, 4}) == {1, 2, 3}
    assert intersection({1, 2, 3, 4}, {3, 2, 1}) == {1, 2, 3}
    assert intersection({1, 2, 3, 4}, {5, 6, 7, 8}) == set()
    assert intersection({1, 2, 3, 4}, {4, 5, 6, 7}) == {4}
    assert intersection({1, 2, 3, 4}, {4, 3, 2, 1}) == {1, 2, 3, 4}
    assert intersection({1, 2, 3, 4}, {1, 2, 3, 4}) == {1, 2, 3, 4}
    assert intersection({1, 2, 3, 4}, {1, 2, 3, 4, 5}) == {1, 2, 3, 4}
    assert intersection({1, 2, 3, 4, 5}, {1, 2, 3, 4}) == {1, 2, 3, 4}
    assert intersection({1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}) == set()
