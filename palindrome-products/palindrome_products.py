from typing import List, Set

def largest_palindrome(max_factor: int, min_factor: int=0) -> List[Set[int]]:
    palindromes = []
    for i in range(max_factor, min_factor, -1):
        for j in range(max_factor, min_factor, -1):
            p = i*j
            if str(p) == str(p)[::-1]:
                palindromes.append(p)
    largest = max(palindromes)
    factors = []
    for i in range(1, largest//2+1):
        if largest%i == 0:
            pair = {i, largest//i}
            factors.append(set((i, largest//i)))
    return largest, factors


def smallest_palindrome():
    pass
