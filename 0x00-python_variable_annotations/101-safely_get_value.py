#!/usr/bin/env python3
"""
101
"""


from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """safely"""
    if key in dct:
        return dct[key]
    else:
        return default
