import copy
import itertools

def activity_selection_brute(start: list[int], finish: list[int]) -> list[int]:
    """
    Given two lists of start and end times for a collection of activities,
    return the optimal set of activities that can be completed without
    overlap.

    This is the brute force solution to the problem.
    """
    if len(start) != len(finish):
        raise ValueError('start and finish arrays must be of the same length!')

    n = len(start)
    activities = list(zip(start, finish))
    perms = itertools.permutations(activities)
    idxs = []

    for perm in perms:
        perm_idxs = [0]
        for idx in range(1, n):
            is_overlapping = False
            for selected_idx in perm_idxs:
                if _is_mutually_overlapping(perm[idx], perm[selected_idx]):
                    is_overlapping = True
                    break

            if not is_overlapping:
                perm_idxs.append(idx)
        
        if len(perm_idxs) > len(idxs):
            idxs = perm_idxs
    
    return idxs

def _is_mutually_overlapping(pair1: tuple[int, int], pair2: tuple[int, int]) -> bool:
    """
    Helper function for determining if start / finish time pairs are mutually
    overlapping for the brute force solution to the Activity Selection Problem.
    """
    return not (pair2[0] > pair1[1] or pair2[1] < pair1[0])

def activity_selection_greedy(start: list[int], finish: list[int]) -> list[int]:
    """
    Given two lists of start and end times for a collection of activities,
    return the optimal set of activities that can be completed without
    overlap.

    This is the greedy solution to the problem.

    NOTE: activities must be ordered by ascending finish date.
    """
    if len(start) != len(finish):
        raise ValueError('start and finish arrays must be of the same length!')

    idxs = [0]
    for i in range(1, len(start)):
        if (start[i] > finish[idxs[-1]]):
            idxs.append(i)

    return idxs

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

def egyptian_fractions(fraction: Fraction) -> list[Fraction]:
    """
    Computes the \"Egyptian Fractions\" for a given Fraction.
    This can be defined as the list of unit fractions (fractions with a
    numerator of 1) that compose the given fraction.
    """
    temp = copy.copy(fraction)
    candidate = Fraction(1, 2)
    components = []

    while temp.numerator != 0:
        if candidate <= temp:
            temp -= candidate
            components.append(copy.copy(candidate))

        candidate.denominator += 1

    return components