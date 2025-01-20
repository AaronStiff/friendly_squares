#!/usr/bin/env python3

import numpy as np
from sympy.utilities.iterables import multiset_permutations as msp
from sympy import binomial
from alive_progress import alive_bar, config_handler
import time

SEQUENCE = [0, 0, 2, 3, 8, 8, 10, 18, 18]
config_handler.set_global(spinner=None, bar="smooth", length=5, refresh_secs=1)


def check_matrix(matrix, size):
    """Takes a numpy array and it's size and returns True if it meets the
    "friendly squares" rules, False if otherwise"""

    shifts = {
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    }
    np_it = np.nditer(matrix, flags=["multi_index"])
    for e in np_it:
        i = np_it.multi_index
        neighbourhood = 0
        for s in shifts:
            if 0 <= i[0] + s[0] <= size - 1 and 0 <= i[1] + s[1] <= size - 1:
                neighbourhood += matrix[i[0] + s[0], i[1] + s[1]]
            if neighbourhood >= 2:
                break
        if neighbourhood < 2:
            return False

    return True


def get_candidates(size):
    """Iterator to get all matrices of given size with the minimum number
    of ones, irrespective of whether they meet the "friendly square" rules."""

    min_ones = SEQUENCE[size]
    elements = [int(i) for i in "1" * min_ones + "0" * (size**2 - min_ones)]
    for p in msp(elements):
        matrix = np.array(p).reshape(size, -1)
        yield matrix


def main(size):
    """Main program. Takes the size of the matrix for which to calculate
    the number of "friendly square" colourings."""

    matches = 0
    total = binomial(size**2, SEQUENCE[size])
    with alive_bar(total=int(total)) as bar:
        for matrix in get_candidates(size):
            if check_matrix(matrix, size):
                matches += 1
            bar()
    return matches


n = 5
print(f"\nTotal valid colourings for a {n}x{n} matrix: {main(n)}")
