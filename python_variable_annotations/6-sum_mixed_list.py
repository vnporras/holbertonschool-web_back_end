#!/usr/bin/env python3
"""
This module provides a sum_mixed_list function to sum a list of
integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floating-point numbers.

    Parameters:
    mxd_lst (List[Union[int, float]]): The list of integers and floats to sum.

    Returns:
    float: The sum of the list of integers and floats.
    """
    return float(sum(mxd_lst))
