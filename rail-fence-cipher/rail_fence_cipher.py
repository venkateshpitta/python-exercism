from typing import List
import itertools

def fence_pattern(lst: List, numrails: int) -> List:
    fence = [[None] * len(lst) for n in range(numrails)]
    rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x

    if 1!=1: # debug
        for rail in fence:
            print (''.join('.' if c is None else str(c) for c in rail))

    return [c for rail in fence for c in rail if c is not None]

def encode(text: str, n: int) -> str:
    return ''.join(fence_pattern(text, n))

def decode(text: str, n: int) -> str:
    rng = range(len(text))
    pos = fence_pattern(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)
