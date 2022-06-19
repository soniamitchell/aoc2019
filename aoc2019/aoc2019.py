"""Provide general helper functions for AoC2019.

This module contains general helper functions for AoC2019.

The module contains the following functions:

- `read_data(path)` - Returns a vector of integers.
"""


def read_data(path):
    """
    Read data from txt file.

    Args:
        path (str): The path name.

    Returns:
        int: A vector of integers.
    """
    with open(path) as f:
        data = [int(x.strip()) for x in f.readlines()]
    return data
