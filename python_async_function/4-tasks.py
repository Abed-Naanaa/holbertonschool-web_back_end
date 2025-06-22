#!/usr/bin/env python3
"""Module to run multiple asyncio tasks"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times and returns results
    in ascending order (no sort).
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
