import string

def score(given: str) -> int:
    letters = string.ascii_lowercase
    numbers = 1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
    table = dict(zip(letters, numbers))
    return sum(table[g] for g in given.lower()) if len(given) > 0 else 0
