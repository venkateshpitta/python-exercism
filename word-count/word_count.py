import re
from itertools import groupby

def word_count(given: str) -> dict:
    given = given.replace(',', ' ').replace('_', ' ')
    words = [re.sub(r'[^a-zA-Z]', '', t) for t in given.lower().split()]
    words[:] = [word for word in words if word != '' and all(w.isalpha() for w in word)]
    return {word:len(list(group)) for word, group in groupby(words)}
