"""
htmlpy.utils
============

Utilities in htmlpy.
"""

from typing import Iterable


def classing(*args):
    """
    Convert all arguments to space joined string.
    ex: ['h1', 'mb-0'] -> "h1 mb-0"
    """

    result = []
    for item in args:
        if isinstance(item, Iterable) and (not isinstance(item, str)):
            item = classing(*item)

        result.append(item)

    return ' '.join(result)
