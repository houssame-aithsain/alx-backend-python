#!/usr/bin/env python3
"""
multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """callable"""
    def _multiplier(n: float) -> float:
        """float"""
        return n * multiplier
    return _multiplier
