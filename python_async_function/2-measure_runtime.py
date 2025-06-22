#!/usr/bin/env python3
"""Module to measure average runtime of async execution"""

import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures total runtime of wait_n and returns avg per coroutine"""
    start = time.time()
    __import__('asyncio').run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
