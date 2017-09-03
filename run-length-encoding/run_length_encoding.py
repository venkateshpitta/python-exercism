import re
from itertools import groupby

def decode(given: str) -> str:
    numbers = (int(n) if n else 1 for n in re.split('\D', given))
    letters = ''.join(n for n in re.split('\d', given) if n)
    return ''.join(number*letter for number,letter in zip(numbers,letters))


def encode(given: str) -> str:
    code = ''
    for letter, group in groupby(given):
        count = len(list(group))
        code += (str(count) if count > 1 else '') + letter
    return code
