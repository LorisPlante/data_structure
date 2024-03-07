from exos.exo18 import parcourir_bytearray

def test_parcourir_bytearray():
    assert parcourir_bytearray(bytearray([1, 2, 3, 4])) == bytearray([2, 3, 4, 5])
    assert parcourir_bytearray(bytearray([0, 0, 0, 0])) == bytearray([1, 1, 1, 1])
    assert parcourir_bytearray(bytearray([1, 1, 1, 1])) == bytearray([2, 2, 2, 2])
    assert parcourir_bytearray(bytearray([2, 2, 2, 2])) == bytearray([3, 3, 3, 3])
    assert parcourir_bytearray(bytearray([3, 3, 3, 3])) == bytearray([4, 4, 4, 4])
    assert parcourir_bytearray(bytearray([4, 4, 4, 4])) == bytearray([5, 5, 5, 5])
    assert parcourir_bytearray(bytearray([5, 5, 5, 5])) == bytearray([6, 6, 6, 6])
    assert parcourir_bytearray(bytearray([6, 6, 6, 6])) == bytearray([7, 7, 7, 7])
    assert parcourir_bytearray(bytearray([7, 7, 7, 7])) == bytearray([8, 8, 8, 8])
    assert parcourir_bytearray(bytearray([8, 8, 8, 8])) == bytearray([9, 9, 9, 9])
    assert parcourir_bytearray(bytearray([9, 9, 9, 9])) == bytearray([10, 10, 10, 10])
    assert parcourir_bytearray(bytearray([10, 10, 10, 10])) == bytearray([11, 11, 11, 11])
    assert parcourir_bytearray(bytearray([11, 11, 11, 11])) == bytearray([12, 12, 12, 12])