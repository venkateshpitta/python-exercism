import re

def word_count(given: str) -> dict:
    words = "".join(c if c.isalnum() else " " for c in given).lower().split()
    return {word:words.count(word) for word in set(words)}
