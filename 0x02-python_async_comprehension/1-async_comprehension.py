#!/usr/bin/env python3
"""
Defines an asynchronous coroutine that collects 10.
using an asynchronous comprehension over async_generator.
"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator,
    and returns them in a list.
    """
    return [number async for number in async_generator()]
