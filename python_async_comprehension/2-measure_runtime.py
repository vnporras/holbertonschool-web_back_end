#!/usr/bin/env python3

import time
from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes the async_comprehension coroutine four times in parallel
    using asyncio.gather, measures the total runtime, and returns it.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()

    total_time = end_time - start_time

    return total_time
