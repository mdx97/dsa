import unittest
from .greedy import activity_selection_brute, activity_selection_greedy

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