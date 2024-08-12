#!/usr/bin/env python3
"""
This module provides a sum_list function to sum a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floating-point numbers.

    Parameters:
    input_list (List[float]): The list of float numbers to sum.

    Returns:
    float: The sum of the list of float numbers.
    """
    return float(sum(input_list))
