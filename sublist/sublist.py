from typing import List

SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)

def check_lists(l1, l2): ## type hinting here will be interesting
    s1, s2 = '_'.join(str(i) for i in l1), '_'.join(str(i) for i in l2)
    if s1 == s2: return EQUAL
    elif s1 in s2: return SUBLIST
    elif s2 in s1: return SUPERLIST
    else: return UNEQUAL
