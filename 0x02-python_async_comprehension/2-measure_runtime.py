#!/usr/bin/env python3
"""Measure the total runtime of executing."""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Runs async_comprehension four times in parallel
    and calculates the total time taken to execute them.

    Returns:
        The total runtime (in seconds) as a float.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
