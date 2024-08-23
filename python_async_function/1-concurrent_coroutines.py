#!/usr/bin/env python3
"""
This module contains an asynchronous routine `wait_n`
that executes multiple `wait_random` coroutines concurrently and
returns the delays in ascending order.
"""

import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    spawn wait_random n times with the specified max_delay.

    Parameters:
    n: int
    max_dalay: int

    Returns:
    return the list of all the delays (float values)
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
