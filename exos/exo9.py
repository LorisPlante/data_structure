#  Écrire un programme qui affiche une pyramide d'étoiles (*). L'utilisateur doit indiquer la hauteur de la pyramide, et le programme génère la pyramide correspondante.

def print_pyramid(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))