from exos.exo2 import ExoString


def test_extract_python():
    exo_string = ExoString()
    exo_string.chaine_donnee = "Python est un langage de programmation puissant et facile à apprendre"
    assert exo_string.extract_python() == "Python"


def test_extract_apprendre():
    exo_string = ExoString()
    exo_string.chaine_donnee = "Python est un langage de programmation puissant et facile à apprendre"
    assert exo_string.extract_apprendre() == "apprendre"


def test_extract_phrase():
    exo_string = ExoString()
    exo_string.chaine_donnee = "Python est un langage de programmation puissant et facile à apprendre"
    assert exo_string.extract_phrase() == "langage de programmation"


def test_extract_inverse():
    exo_string = ExoString()
    exo_string.chaine_donnee = "Python est un langage de programmation puissant et facile à apprendre"
    assert exo_string.extract_inverse() == "erdnerppa à elicaf te tnassiup noitammargorp ed egagnal nu tse nohtyP"
