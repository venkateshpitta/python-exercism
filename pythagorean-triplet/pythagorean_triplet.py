import math
from typing import Tuple, List, Set
Triplet = Tuple[int, int, int]
Pair = Tuple[int, int]

def primitive_triplets(b: int) -> Set[Triplet]:
    if b%4 != 0:
        raise ValueError('Cannot find triplets starting with number non-divisible by 4')
    ## b = 2mn; m > 1, n > 1
    mn = b // 2
    out = set()
    for m in range(1, mn+1):
        n = b//(2*m)
        if m - n > 0 and 2*m*n==b:
            a = m**2 + n**2
            c = m**2 - n**2
            if math.gcd(a,b) == math.gcd(b,c) == math.gcd(c,a) == 1:
                out.add(tuple(sorted((a,b,c))))
    return out


def triplets_in_range(begin: int, end: int) -> Set[Triplet]:
    out = set()
    potential_bs = [b for b in range(begin, end+1) if b%4 == 0]
    def factorise(num: int) -> Set[int]:
        limit = num+1
        factors = set()
        for i in range(2, limit):
            if num%i == 0:
                factors.add(i)
        factors.add(1)
        return factors

    def in_legal_range(triple: Triplet) -> bool:
        return all(t in range(begin, end+1) for t in triple)

    for b in potential_bs:
        factors = factorise(b//2)
        for m in factors:
            n = b//(2*m)
            if m - n <= 0: continue
            if 2*m*n == b and any(f%2==0 for f in (m, n)):
                a, c = m**2 + n**2, m**2 - n**2
                if in_legal_range((a,b,c)) and is_triplet((a,b,c)):
                    out.add(tuple(sorted((a,b,c))))

    temp = set()
    for triple in out:
        for i in range(2, 10):
            a, b, c = (t*i for t in triple)
            if in_legal_range((a,b,c)) and is_triplet((a,b,c)):
                temp.add(tuple(sorted((a,b,c))))

    for triple in temp:
        out.add(triple)

    for b in potential_bs:
        for a in range(begin if begin%2==1 else begin+1, end+1, 2):
            for c in range(begin if begin%2==1 else begin+1, end+1, 2):
                if in_legal_range((a,b,c)) and is_triplet((a,b,c)):
                    out.add(tuple(sorted((a,b,c))))
    return out


def is_triplet(t: Triplet) -> bool:
    a, b, c = sorted(t)
    tr1 = math.gcd(a,b) == math.gcd(b,c) == math.gcd(c,a)
    tr2 = c**2 == a**2 + b**2
    return tr1 and tr2
