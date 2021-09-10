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