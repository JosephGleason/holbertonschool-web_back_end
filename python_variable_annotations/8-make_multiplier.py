#!/usr/bin/env python3

"""
This module defines a function that returns a multiplier function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
