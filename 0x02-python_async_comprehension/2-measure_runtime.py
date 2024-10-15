#!/usr/bin/env python3
"""
Defines a coroutine that measures the total runtime for running
async_comprehension four times in parallel.
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures
    the total runtime.

    Returns:
        Total runtime for four async_comprehension calls.
    """
    start_time = time.time()  # Record the start time

    # Run async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in 4))

    total_time = time.time() - start_time  # Calculate the total elapsed time
    return total_time
