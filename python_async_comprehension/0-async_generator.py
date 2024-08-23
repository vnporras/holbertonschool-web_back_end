#!/usr/bin/env python3

"""
This module contains an asynchronous generator function.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates ten random floating-point numbers
    between 0 and 10.

    The function sleeps for 1 second between each yield and yields a new
    random number each time. The total count of yielded values is ten.

    Returns:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
