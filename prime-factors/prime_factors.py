from typing import List
import prime_tools ## pip install prime_tools

def prime_factors(n: int) -> List[int]:
    pith = prime_tools.prime_factorization.list_prime_factors(n)
    out = []
    for prime in pith:
        while n%prime == 0:
            out.append(prime)
            n //= prime
    return out
