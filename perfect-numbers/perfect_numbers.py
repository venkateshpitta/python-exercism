def divisor_generator():
    pass


def is_perfect(n: int) -> bool:
    return n == sum(filter(lambda t: n%t==0, range(1,n//2+1)))
