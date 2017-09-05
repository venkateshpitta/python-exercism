def on_square(n: int) -> int:
    if n < 1 or n > 64: raise ValueError
    return 2**(n-1)


def total_after(n: int) -> int:
    if n < 1 or n > 64: raise ValueError
    return (1 - 2**n) // (1 - 2)
