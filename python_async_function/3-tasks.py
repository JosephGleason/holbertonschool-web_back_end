#!/usr/bin/env python3
"""3-tasks module: creates an asyncio Task from wait_random."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio.Task that runs wait_random with given max_delay.

    Args:
        max_delay (int): Maximum delay to wait.

    Returns:
        asyncio.Task: The scheduled coroutine task.
    """
    return asyncio.create_task(wait_random(max_delay))
