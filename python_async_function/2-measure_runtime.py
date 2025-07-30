#!/usr/bin/env python3
"""2-measure_runtime module: measures execution time of wait_n."""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average runtime per coroutine for wait_n.

    Args:
        n (int): number of concurrent coroutines
        max_delay (int): maximum delay passed to wait_random

    Returns:
        float: average execution time per coroutine
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total_time = end - start
    return total_time / n
