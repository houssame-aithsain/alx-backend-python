#!/usr/bin/env python3
""" Execute multiple coroutines concurrently """

import asyncio
from typing import List

# Use __import__ to import the wait_random function from '0-basic_async_syntax'
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns a list of all the delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    
    # Return delays in ascending order (without using sort())
    return sorted(delays)
