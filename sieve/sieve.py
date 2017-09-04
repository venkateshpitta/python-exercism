from typing import List

def sieve(n: int) -> List[int]:
    if n < 2: return []
    knowns = [2]
    potentials = list(range(3, n+1, 2))
    while len(potentials) > 0:
        knowns.append(potentials[0])
        potentials = [p for p in potentials[1:] if p%knowns[-1] != 0]
    return knowns
