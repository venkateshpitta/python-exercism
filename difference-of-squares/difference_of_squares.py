def square_of_sum(n: int) -> int:
    s = n * (n + 1) / 2
    return s**2


def sum_of_squares(n: int) -> int:
    return n * (n + 1) * (2 * n + 1) / 6


def difference(n: int) -> int:
    return square_of_sum(n) - sum_of_squares(n)
