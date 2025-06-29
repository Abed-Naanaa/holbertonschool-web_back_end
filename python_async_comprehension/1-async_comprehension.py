#!/usr/bin/env python3
"""Module that defines a  using async comprehension."""

from typing import List
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    """Collect 10 random floats fr and return them."""
    return [i async for i in async_generator()]
