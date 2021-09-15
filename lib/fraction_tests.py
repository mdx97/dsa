import unittest
from .fraction import Fraction

class TestFraction(unittest.TestCase):
    def test_le(self):
        self.assertTrue(Fraction(1, 3) <= Fraction(1, 2))
        self.assertTrue(Fraction(1, 2) <= Fraction(1, 2))
        self.assertTrue(Fraction(1, 2) <= Fraction(2, 4))
        self.assertFalse(Fraction(1, 2) <= Fraction(1, 3))
        self.assertFalse(Fraction(3, 6) <= Fraction(33, 99))
    
    def test_sub(self):
        self.assertEqual(Fraction(1, 2), Fraction(1, 2) - Fraction(0, 2))
        self.assertEqual(Fraction(1, 2), Fraction(3, 4) - Fraction(1, 4))
        self.assertEqual(Fraction(1, 12), Fraction(9, 12) - Fraction(2, 3))
        self.assertEqual(Fraction(3, 4), Fraction(19, 23) - Fraction(7, 92))

if __name__ == '__main__':
    unittest.main()