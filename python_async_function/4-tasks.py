#!/usr/bin/env python3
"""
Execute multiple coroutines concurrently and return delays in ascending order.
"""

import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Spawn `n` coroutines each waiting up to `max_delay` seconds, and return
    the delays in ascending order.

    Parameters:
    n (int): Number of coroutines to spawn.
    max_delay (int): Maximum delay time for each coroutine.

    Returns:
    typing.List[float]: Sorted list of delays.
    """
    delays = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

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
