import math
from typing import Tuple, List
Triplet = Tuple[int, int, int]

def primitive_triplets(n: int) -> List[Triplet]:
    if n%4 != 0:
        raise ValueError('Cannot find triplets starting with number non-divisible by 4')


def triplets_in_range():
    pass


def is_triplet(t: Triplet) -> bool:
    return 1 == math.gcd(t[0], math.gcd(t[1], t[2]))
