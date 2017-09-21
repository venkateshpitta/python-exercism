from typing import List, Set, Tuple

def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]

def all_products(finish: int, start: int=1) -> List[Tuple[int, Tuple[int, int]]]:
    return [(i*j, (i, j)) for i in range(start, finish+1) for j in range(start, finish+1) if is_palindrome(i*j)]
    # out = [(i*j, (i, j)) for i in range(start, finish+1) for j in range(start, finish+1) if is_palindrome(i*j)]
    # print('out = {out}'.format(out=out))
    # return out

def largest_palindrome(max_factor: int, min_factor: int=1) -> Tuple[int, Tuple[int, int]]:
    return max([s for s in all_products(start=min_factor, finish=max_factor)], key=lambda x: x[0])

def smallest_palindrome(max_factor: int, min_factor: int=1) -> Tuple[int, Tuple[int, int]]:
    return min(all_products(start=min_factor, finish=max_factor), key=lambda x: x[0])
