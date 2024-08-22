#!/usr/bin/env python3
"""
This module contains an asynchronous routine `wait_n` that executes multiple
`wait_random` coroutines concurrently and returns the delays in ascending order.
"""

import asyncio
from typing import List
import importlib

module_name = "0-basic_async_syntax"
wait_random = importlib.import_module(module_name).wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]

    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
