#!/usr/bin/env python3
"""
This module provides an element_length function that returns a list of tuples.
Each tuple contains an element from the input iterable and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from
    the input iterable and the length of that element.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequence elements.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, each containing a
    sequence element from lst and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
