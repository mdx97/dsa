import math

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __sub__(self, other):
        common_denominator = self.denominator * other.denominator
        self_numerator = self.numerator * other.denominator
        other_numerator = other.numerator * self.denominator
        return _simplify_fraction(Fraction(self_numerator - other_numerator, common_denominator))

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

def _simplify_fraction(fraction: Fraction) -> Fraction:
    """Returns a mathematically simplified version of the given Fraction."""
    numerator_factors = _factorize(fraction.numerator)
    denominator_factors = _factorize(fraction.denominator)
    gcf = list(sorted(numerator_factors.intersection(denominator_factors)))[-1]
    return Fraction(fraction.numerator // gcf, fraction.denominator // gcf)

def _factorize(number: int) -> set[int]:
    """Returns a set of the factors for the given number."""
    factors = set([1, number])
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    
    return factors