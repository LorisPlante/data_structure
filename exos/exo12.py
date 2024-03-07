def count_palindromes(words):
    return sum(word == word[::-1] for word in words)
