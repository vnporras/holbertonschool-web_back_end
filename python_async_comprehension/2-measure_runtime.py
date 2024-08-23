#!/usr/bin/env python3
"""
Run time for four parallel comprehensions

measure_runtime routine that will execute async_comprehension four
times in parallel using asyncio.gather. measure_runtime measures
the total execution time and returns it.
"""
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
