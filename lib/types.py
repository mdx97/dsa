import copy

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

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
    # TODO: Actually simplify.
    return copy.copy(fraction)
