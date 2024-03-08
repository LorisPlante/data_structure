from exos.exo4 import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_remove_duplicates_bis():
    assert remove_duplicates([1, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
