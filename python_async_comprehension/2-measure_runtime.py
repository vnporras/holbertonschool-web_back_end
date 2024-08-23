#!/usr/bin/env python3

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes the async_comprehension coroutine four times in parallel
    using asyncio.gather, measures the total runtime, and returns it.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    return end_time - start_time
