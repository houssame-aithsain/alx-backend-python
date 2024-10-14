#!/usr/bin/env python3
"""
Measures the average runtime of wait_n for n executions.
"""


import time
import asyncio
from typing import List


# Import wait_n from the previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per coroutine.
    """
    start_time = time.time()  # Record start time
    asyncio.run(wait_n(n, max_delay))  # Run the asynchronous wait_n function
    end_time = time.time()  # Record end time

    total_time = end_time - start_time  # Calculate total elapsed time
    return total_time / n  # Return the average time per coroutine
