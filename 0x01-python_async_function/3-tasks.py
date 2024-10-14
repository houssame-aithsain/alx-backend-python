#!/usr/bin/env python3
"""
Returns an asyncio Task for wait_random.
"""


import asyncio


# Import wait_random from the previous file
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a Task object that schedules.
    """
    return asyncio.create_task(wait_random(max_delay))
