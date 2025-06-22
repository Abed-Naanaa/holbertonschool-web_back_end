#!/usr/bin/env python3
"""Module for concurrent coroutine execution"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times and returns list of delays
    in ascending order without using sort().
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    results = []
    for task in asyncio.as_completed(delays):
        result = await task
        results.append(result)
    return results
