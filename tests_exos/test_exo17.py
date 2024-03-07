# teste de # Écrivez un programme qui crée un bytearray à partir d'une liste d'entiers, puis modifie un de ses éléments.
#
# def create_bytearray_from_list_of_integers(list_of_integers):
#     return bytearray(list_of_integers)

from exos.exo17 import create_bytearray_from_list_of_integers

def test_create_bytearray_from_list_of_integers():
    assert create_bytearray_from_list_of_integers([1, 2, 3]) == bytearray(b'\x01\x02\x03')
    assert create_bytearray_from_list_of_integers([1, 2, 3, 4]) == bytearray(b'\x01\x02\x03\x04')
    assert create_bytearray_from_list_of_integers([1, 2, 3, 4, 5]) == bytearray(b'\x01\x02\x03\x04\x05')
    assert create_bytearray_from_list_of_integers([1, 2, 3, 4, 5, 6]) == bytearray(b'\x01\x02\x03\x04\x05\x06')
    assert create_bytearray_from_list_of_integers([1, 2, 3, 4, 5, 6, 7]) == bytearray(b'\x01\x02\x03\x04\x05\x06\x07')
    assert create_bytearray_from_list_of_integers([1, 2, 3, 4, 5, 6, 7, 8]) == bytearray(b'\x01\x02\x03\x04\x05\x06\x07\x08')
    assert create_bytearray_from_list_of_integers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == bytearray(b'\x01\x02\x03\x04\x05\x06\x07\x08\t')
    assert create_bytearray_from_list_of_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == bytearray(b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n')
    assert create_bytearray_from_list_of_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == bytearray(b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b')