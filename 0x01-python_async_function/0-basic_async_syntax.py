#!/usr/bin/env python3
"""
asyncio
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """sleep float numb"""
    rand_num: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand_num)
    return rand_num
