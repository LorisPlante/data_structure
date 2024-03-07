# test de # Écrivez un programme qui retourne la différence symétrique entre deux ensembles.
#
# def symmetric_difference(set1, set2):
#     return set1 ^ set2

from exos.exo16 import symmetric_difference

def test_symmetric_difference():
    assert symmetric_difference({1, 2, 3}, {2, 3, 4}) == {1, 4}