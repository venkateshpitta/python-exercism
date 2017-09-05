from functools import reduce
from operator import mul

def largest_product(string: str, size: int) -> int:
    if size > len(string) or size < 0: raise ValueError
    if size == 0: return 1
    chunks = []
    for i in range(0, len(string)-(size-1)):
        temp = [int(x) for x in string[i:i+size]]
        chunks.append(reduce(mul, temp))
    return max(chunks)
