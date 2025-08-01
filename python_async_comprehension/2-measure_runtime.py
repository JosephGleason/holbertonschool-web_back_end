#!/usr/bin/env python3
"""Module for measure_runtime coroutine.
This module provides a coroutine to measure the runtime
of running async_comprehension in parallel.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of running async_comprehension
    four times in parallel using asyncio.gather.
    Returns:
        float: total elapsed time in seconds
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
