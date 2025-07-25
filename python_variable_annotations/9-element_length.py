#!/usr/bin/env python3
"""Module that annotates a function returning list of element lengths."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with elements and their lengths.
    """
    return [(i, len(i)) for i in lst]
