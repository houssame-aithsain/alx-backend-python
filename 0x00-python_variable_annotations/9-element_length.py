#!/usr/bin/env python3
"""
lenght
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """annotation"""
    return [(i, len(i)) for i in lst]
