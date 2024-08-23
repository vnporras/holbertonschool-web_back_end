#!/usr/bin/env python3
"""
This function calculates the total time taken to run the
`wait_n` coroutine, which spawns `n` instances of `wait_random`
with a maximum delay of `max_delay`.
It then returns the average time per coroutine.
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time taken to execute the `wait_n` coroutine.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average time (in seconds) per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
