#!/usr/bin/env python3
"""
Takes 2 int arguments: n and max_delay.
Spawns n tasks that wait for a random delay (up to max_delay)
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Runs multiple coroutines concurrently, each waiting for a random delay.
    Collects all delays and returns them in ascending order.
    """
    # Create tasks for all coroutines and run them concurrently
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Wait for all tasks to complete and gather the results
    delays = await asyncio.gather(*tasks)

    # Return the list of delays sorted in ascending order
    return sorted(delays)
