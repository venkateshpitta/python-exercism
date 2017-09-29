import math
from typing import Union

number = Union[int, float]

class ComplexNumber(object):
    def __init__(self, real: number, imaginary: number) -> None:
        self.real, self.imaginary = real, imaginary

    def add(self, other):
        assert(isinstance(other, ComplexNumber))
        return ComplexNumber((self.real + other.real), (self.imaginary + other.imaginary))

    def mul(self, other):
        assert(isinstance(other, ComplexNumber))
        return ComplexNumber((self.real * other.real - self.imaginary * other.imaginary),
                             (self.real * other.imaginary + self.imaginary * other.real))

    def sub(self, other):
        assert(isinstance(other, ComplexNumber))
        return ComplexNumber((self.real - other.real), (self.imaginary - other.imaginary))

    def div(self, other):
        ## What is wrong here? test_multiply_numbers_with_real_and_imaginary_part(self): always fails
        assert(isinstance(other, ComplexNumber))
        den = other.real**2 + other.imaginary**2
        r = self.real * other.real + self.imaginary * other.imaginary
        i = self.imaginary * other.real - self.real * other.imaginary
        return ComplexNumber((r/den), (i/den))

    def abs(self) -> number:
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imaginary)

    def exp(self):
        return ComplexNumber((math.exp(self.real) * math.cos(self.imaginary)),
                             int(math.exp(self.real) * math.sin(self.imaginary)))
