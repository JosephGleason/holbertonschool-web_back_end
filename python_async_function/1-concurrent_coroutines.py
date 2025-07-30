#!/usr/bin/env python3
"""1-concurrent_coroutines module: run wait_random n times concurrently."""

import asyncio
from typing import List
from importlib import import_module


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Runs wait_random n times concurrently with the given max_delay.

    Args:
        n (int): Number of coroutines to launch.
        max_delay (int): Max delay for each coroutine.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
