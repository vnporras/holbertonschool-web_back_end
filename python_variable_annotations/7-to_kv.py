#!/usr/bin/env python3
"""
This module provides a to_kv function that returns a tuple
with a string and the square of an int/float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of the given int/float.

    Parameters:
    k (str): The string to include in the tuple.
    v (Union[int, float]): The integer or float whose
    square is to be calculated.

    Returns:
    Tuple[str, float]: A tuple where the
    first element is the string k and the second element
    is the square of v as a float.
    """
    return (k, float(v ** 2))
