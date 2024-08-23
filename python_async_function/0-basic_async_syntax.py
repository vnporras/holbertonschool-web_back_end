#!/usr/bin/env python3
"""
This function takes an integer argument `max_delay`
(with a default value of 10) and waits for a random time between 0 and
`max_delay` seconds (including decimal values).
After the wait, the function returns the actual delay time.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Spawn `wait_random` n times with the specified `max_delay`.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        List[float]: A list of all the delay times in ascending order.
    """
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]

    for delay in await asyncio.gather(*tasks):
        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays
