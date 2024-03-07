source = "Ceci est un Test de la Chaîne de Caractères!"


def count_upper_lower_case(source):
    upper = 0
    lower = 0
    for char in source:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return f"Il y a {upper} majuscules, et {lower} minuscules."