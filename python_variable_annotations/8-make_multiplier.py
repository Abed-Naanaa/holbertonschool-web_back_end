#!/usr/bin/env python3
"""Module with a function returning a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.
    """
    def multiply(n: float) -> float:
        """Multiply the float n by multiplier."""
        return n * multiplier

    return multiply
