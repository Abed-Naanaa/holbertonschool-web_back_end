#!/usr/bin/env python3
"""Module that defines a coroutine to measure runtime of parallel async comprehensions."""

import asyncio
import time
from typing import Callable
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """Measure the total runtime of executing async_comprehension four times in parallel and return it."""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
