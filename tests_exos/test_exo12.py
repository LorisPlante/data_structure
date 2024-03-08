from exos.exo12 import count_palindromes


def test_count_palindromes_five():
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor"]) == 5


def test_count_palindromes_six():
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor", "hello", "world", "madam"]) == 6


def test_count_palindromes_seven():
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor", "hello", "world", "madam", "racecar"]) == 7


def test_count_palindromes_ten():
    assert count_palindromes(["kayak", "tenet", "radar", "level", "rotor", "hello", "world", "madam", "racecar", "civic", "deified", "noon"]) == 10
