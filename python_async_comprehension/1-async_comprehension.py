#!/usr/bin/env python3

"""
This module contains an asynchronous generator function.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random floating-point numbers between 0 and 10
    using an asynchronous comprehension over the `async_generator` function.

    Returns:
        List[float]: A list containing 10 random floating-point numbers.
    """
    return [number async for number in async_generator()]
