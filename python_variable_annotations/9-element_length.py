#!/usr/bin/env python3
"""Module that defines a function to return elements with their lengths."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element in iterable and length.
    """
    return [(i, len(i)) for i in lst]
