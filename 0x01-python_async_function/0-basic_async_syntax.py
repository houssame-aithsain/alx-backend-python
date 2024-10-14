#!/usr/bin/env python3
"""
async
"""


import asyncio, random


async def wait_random(max_delay = 10):
    """sleep float numb"""
    rand_num = random.uniform(0, max_delay)
    await asyncio.sleep(rand_num)
    return rand_num
