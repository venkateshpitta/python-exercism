def divisor_generator():
    pass


def is_perfect(n: int) -> bool:
    return n == sum(list(f for i in range(1, int(n**0.5)+1) if n%i==0 for f in (i, n//i))) - n
