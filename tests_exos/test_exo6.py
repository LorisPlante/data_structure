from exos.exo6 import find_largest_tuple

def test_find_largest_tuple():
    assert find_largest_tuple([(1, 2, 3), (4, 5), (6, 7, 8, 9)]) == (6, 7, 8, 9)

def test_find_largest_tuple_without_anyone():
    assert find_largest_tuple([]) == None

def test_find_largest_tuple_all_equal():
    assert find_largest_tuple([(1, 2), (3, 4), (5, 6)]) == (1, 2)

def test_find_largest_tuple_all_empty():
    assert find_largest_tuple([(), (), ()]) == ()

