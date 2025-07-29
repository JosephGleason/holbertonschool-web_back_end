#!/usr/bin/env python3
"""
This module defines a function that returns a tuple containing
a string and the square of a numeric value as a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k and the square of v as a float.
    """
    return (k, float(v * v))
