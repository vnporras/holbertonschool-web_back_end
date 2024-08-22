#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine `wait_random` that waits
for a random delay and returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay
    seconds and returns the delay.

    Args:
        max_delay (int): The maximum number of seconds to wait.
        Defaults to 10.

    Returns:
        float: The actual delay time.
    """
    random.seed(0)
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
