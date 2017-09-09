import math
from typing import Tuple
Triplet = Tuple[int, int, int]

def primitive_triplets():
    pass


def triplets_in_range():
    pass


def is_triplet(t: Triplet) -> bool:
    return 1 == math.gcd(t[0], math.gcd(t[1], t[2]))
