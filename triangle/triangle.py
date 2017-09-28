from typing import Union

number = Union[int, float]

class TriangleError(Exception):
    pass


class Triangle(object):
    def __init__(self, a: number, b: number, c: number) -> None:
        longest = max(a,b,c)
        if longest >= (a + b + c) - longest: raise TriangleError
        self.a, self.b, self.c = a, b, c
    
    def kind(self) -> str:
        if self.a == self.b == self.c: return "equilateral"
        if self.a == self.b or self.b == self.c or self.a == self.c: return "isosceles"
        return "scalene"
