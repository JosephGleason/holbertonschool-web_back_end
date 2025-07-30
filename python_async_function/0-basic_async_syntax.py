#!/usr/bin/env python3
"""0-basic_async_syntax module: contains the wait_random coroutine."""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:

    """Asynchronously waits for a random delay between 0 and max_delay
    and returns the delay time as a float.

    Args:
        max_delay (int): Maximum number of seconds to wait (default is 10).

    Returns:
        float: The actual number of seconds waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
