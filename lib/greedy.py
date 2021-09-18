import copy
import itertools
from .fraction import Fraction

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

def egyptian_fractions(fraction: Fraction) -> list[Fraction]:
    """
    Computes the "Egyptian Fractions" for a given Fraction.
    This can be defined as the list of unit fractions (fractions with a
    numerator of 1) whose sum equals the given fraction.
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

def job_sequencing_problem_greedy(jobs: list[tuple[str, int, int]]) -> list[str]:
    """
    Given a list of jobs and their deadline and profit values, select the
    sequence of jobs that produce the maximum amount of profit. This assumes
    that only one job can be worked at a time.

    The result is returned in sorted order.
    """
    n = max(jobs, key=lambda job: job[1])[1] + 1
    sorted_jobs = list(reversed(sorted(jobs, key=lambda job: job[2])))
    slots = ['' for _ in range(n)]

    for job in sorted_jobs:
        for j in range(job[1], 0, -1):
            if not slots[j]:
                slots[j] = job[0]
                break
    
    return list(filter(lambda slot: slot != '', slots))
