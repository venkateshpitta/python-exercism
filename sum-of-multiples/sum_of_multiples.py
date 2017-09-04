from typing import List

def sum_of_multiples(n: int, ms: List[int]) -> int:
    s = set()
    for m in ms:
        for i in range(1,n):
            if i%m == 0:
                s.add(i)
    return sum(s)
