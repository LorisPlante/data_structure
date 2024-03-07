# Écrivez un programme qui parcourt un bytearray, affiche chaque élément, puis ajoute 1 à chaque élément.

def parcourir_bytearray(bytearray):
    for i in bytearray:
        print(i)
    for i in range(len(bytearray)):
        bytearray[i] += 1
    return bytearray