from typing import List

def slices(num: str, size: int) -> List[List[int]]:
    if size == 0: raise ValueError('Cannot have zero length numbers')
    if size > len(num): raise ValueError('Cannot have slice longer than original number')

    out = []
    for i in range(0, len(num)-(size-1)):
        temp = [int(n) for n in num[i:i+size]]
        out.append(temp)

    return out
