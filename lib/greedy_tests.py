import unittest
from .greedy import activity_selection_brute, activity_selection_greedy, egyptian_fractions, job_sequencing_problem_greedy
from .fraction import Fraction

class ActivitySelectionTests(unittest.TestCase):
    def test_activity_selection_brute(self):
        start = [1, 3, 0, 5, 8, 5]
        finish = [2, 4, 6, 7, 9, 9]
        optimal = activity_selection_brute(start, finish)
        self.assertEqual([0, 1, 3, 4], optimal)

    def test_activity_selection_greedy(self):
        start = [1, 3, 0, 5, 8, 5]
        finish = [2, 4, 6, 7, 9, 9]
        optimal = activity_selection_greedy(start, finish)
        self.assertEqual([0, 1, 3, 4], optimal)
    
    def test_egyptian_fractions(self):
        # Some tests require fraction simplification.

        ans1 = egyptian_fractions(Fraction(2, 3))
        # ans2 = egyptian_fractions(Fraction(6, 14))
        # ans3 = egyptian_fractions(Fraction(12, 13))

        self.assertEqual(2, len(ans1))
        # self.assertEqual(3, len(ans2))
        # self.assertEqual(4, len(ans3))

        self.assertEqual(1, ans1[0].numerator)
        self.assertEqual(2, ans1[0].denominator)
        self.assertEqual(1, ans1[1].numerator)
        self.assertEqual(6, ans1[1].denominator)

        # self.assertEqual(1, ans2[0].numerator)
        # self.assertEqual(3, ans2[0].denominator)
        # self.assertEqual(1, ans2[1].numerator)
        # self.assertEqual(11, ans2[1].denominator)
        # self.assertEqual(1, ans2[2].numerator)
        # self.assertEqual(231, ans2[2].denominator)

        # self.assertEqual(1, ans3[0].numerator)
        # self.assertEqual(2, ans3[0].denominator)
        # self.assertEqual(1, ans3[1].numerator)
        # self.assertEqual(3, ans3[1].denominator)
        # self.assertEqual(1, ans3[2].numerator)
        # self.assertEqual(12, ans3[2].denominator)
        # self.assertEqual(1, ans3[3].numerator)
        # self.assertEqual(156, ans3[3].denominator)
    
    def test_job_sequencing_problem(self):
        jobs = [('a', 4, 20), ('b', 1, 10), ('c', 1, 40), ('d', 1, 30)]
        self.assertCountEqual(['c', 'a'], job_sequencing_problem_greedy(jobs))

        jobs = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
        self.assertCountEqual(['a', 'c', 'e'], job_sequencing_problem_greedy(jobs))

if __name__ == '__main__':
    unittest.main()
