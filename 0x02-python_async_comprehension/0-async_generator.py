#!/usr/bin/env python3
"""
Defines an asynchronous generator that yields a random number.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously yields a random float between 0 and 10, 10 times, 
    waiting 1 second between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait asynchronously for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
