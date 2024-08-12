#!/usr/bin/env python3
"""
This module provides a make_multiplier function that returns a
function to multiply a float by a multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float by the multiplier.

    Parameters:
    multiplier (float): The multiplier to use in the returned function.

    Returns:
    Callable[[float], float]: A function that multiplies a
    float by the multiplier.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier

    return multiplier_function
