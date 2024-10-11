#!/usr/bin/env python3
"""
safe
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe_first"""
    if lst:
        return lst[0]
    else:
        return None
