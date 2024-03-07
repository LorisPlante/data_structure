from exos.exo1 import count_upper_lower_case


def test_count_upper_lower_case_mixedCases():
    source1 = "Ceci est un Test de la Chaîne de Caractères!"
    assert count_upper_lower_case(source1) == "Il y a 4 majuscules, et 31 minuscules."

def test_count_upper_lower_case_none():
    source2 = ""
    assert count_upper_lower_case(source2) == "Il y a 0 majuscules, et 0 minuscules."

def test_count_upper_lower_case_caps():
    source3 = "TEST"
    assert count_upper_lower_case(source3) == "Il y a 4 majuscules, et 0 minuscules."

def test_count_upper_lower_case_low():
    source4 = "test"
    assert count_upper_lower_case(source4) == "Il y a 0 majuscules, et 4 minuscules."

def test_count_upper_lower_case_specials():
    source5 = "123!@#"
    assert count_upper_lower_case(source5) == "Il y a 0 majuscules, et 0 minuscules."

def test_count_upper_lower_case_allMixed():
    source6 = "AbC123!@#"
    assert count_upper_lower_case(source6) == "Il y a 2 majuscules, et 1 minuscules."
