#!/usr/bin/env python3
"""Module that defines a coroutine to collect 10 random numbers using async comprehension."""

from typing import List
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    """Collect 10 random floats from async_generator using async comprehension and return them."""
    return [i async for i in async_generator()]
