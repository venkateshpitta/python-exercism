import functools
from typing import List

def is_prime(knowns: List[int], num: int) -> bool:
    return 0 == len([k for k in knowns if k <= num and num%k == 0])


def memoize(func):
    cache = func.cache = {}
    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoized_func

@memoize
def find_next_few_primes(primes: List[int]) -> List[int]:
    limit = primes[-1] ** 2
    new = [i for i in range(primes[-1], limit, 2) if is_prime(primes, i)]
    return primes + new


@memoize
def nth_prime(n: int) -> int:
    if n < 1: raise ValueError('Non negative numbers only please')
    primes = [2, 3]
    while len(primes) <= n:
        primes = find_next_few_primes(primes)
    return primes[n-1]
