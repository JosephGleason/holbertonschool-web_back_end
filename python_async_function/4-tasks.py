#!/usr/bin/env python3
"""4-tasks module: runs task_wait_random n times concurrently."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Runs task_wait_random n times and returns delays in order.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Max delay for each task.

    Returns:
        List[float]: Delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
