"""
pyplater.utils
===============

Utilities in pyplater.
"""

from collections import UserDict
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


class Props(UserDict):
    def __getattr__(self, key):
        return self.get(key, "")
