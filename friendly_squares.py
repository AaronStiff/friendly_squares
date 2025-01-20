#!/usr/bin/env python3

import numpy as np
from sympy import binomial
from alive_progress import alive_bar, config_handler
import time
from mpermute import mperms as msp

# Minimum number of coloured squares/kings, see https://oeis.org/A379726
SEQUENCE = [0, 0, 2, 3, 8, 8, 10, 18, 18]

# Progress bar settings. refresh_secs should be kept low to prevent slowdown.
config_handler.set_global(spinner=None, bar="smooth", length=5, refresh_secs=1)


def check_matrix(matrix, size):
    """Takes a numpy array and it's size and returns True if it meets the
    "friendly squares" rules, False if otherwise"""

    # All possible coordinate shifts to check neighbouring squares
    # Having (0,0) as the first shift checks the square itself first,
    # hopefully reducing checking time for coloured squares
    shifts = [
        (0, 0),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    # Initialize numpy iterator
    np_it = np.nditer(matrix, flags=["multi_index"])
    # Check each squares
    for e in np_it:
        i = np_it.multi_index
        neighbourhood = 0
        # Check neighbours
        for s in shifts:
            # But only the ones within the bounds of the grid
            if 0 <= i[0] + s[0] <= size - 1 and 0 <= i[1] + s[1] <= size - 1:
                neighbourhood += matrix[i[0] + s[0], i[1] + s[1]]
            # Stop checking neigbours as soon as 2 coloured squares are found
            if neighbourhood >= 2:
                break
        # Reject grid as soon as a square doesn't meet the rules
        if neighbourhood < 2:
            return False

    return True


def get_candidates(size):
    """Iterator to get all matrices of given size with the minimum number
    of ones, irrespective of whether they meet the "friendly square" rules."""

    # Generate the contents of a grid based on the minimum number of ones
    min_ones = SEQUENCE[size]
    elements = [int(i) for i in "1" * min_ones + "0" * (size**2 - min_ones)]
    # Lazily generate all multiset permutations of the contents
    for p in msp(elements):
        # Reshape the contents into a matrix representing the grid
        matrix = np.array(p).reshape(size, -1)
        yield matrix


def main(size):
    """Main program. Takes the size of the matrix for which to calculate
    the number of "friendly square" colourings."""

    # Start counting valid colourings and calculate total candidate grids
    matches = 0
    total = binomial(size**2, SEQUENCE[size])
    # Use progress bar
    with alive_bar(total=int(total)) as bar:
        # Go through each candidate, check, and count if valid
        for matrix in get_candidates(size):
            if check_matrix(matrix, size):
                matches += 1
            # Update progress bar
            bar()
    return matches


n = 6
print(f"\nTotal valid colourings for a {n}x{n} matrix: {main(n)}")
