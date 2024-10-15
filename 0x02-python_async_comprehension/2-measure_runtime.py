#!/usr/bin/env python3
"""Measure the total runtime of executing async_comprehension multiple times."""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Runs async_comprehension four times in parallel using asyncio.gather
    and calculates the total time taken to execute them.

    Returns:
        The total runtime (in seconds) as a float.
    """
    start_time = time.perf_counter()  # Start the timer

    # Execute async_comprehension four times concurrently
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    # Calculate the elapsed time by subtracting start_time from current time
    total_runtime = time.perf_counter() - start_time

    return total_runtime
