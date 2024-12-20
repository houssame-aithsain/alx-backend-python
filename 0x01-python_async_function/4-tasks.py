#!/usr/bin/env python3
"""
Executes multiple coroutines using task_wait_random and.
"""


import asyncio
from typing import List


# Import task_wait_random from the previous file
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawns task_wait_random n times with the specified.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*tasks)  # Wait for all tasks to complete

    return sorted(delays)  # Return delays sorted in ascending order
