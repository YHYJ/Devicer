#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2019-03-28 10:12:31

keyvalue code --> keyvalue
"""

from swipe.utils import KEY_CODE


def kvc2kv(code: int):
    """Keyvalue code to keyvalue.

    :code: int: keyvalue code
    :returns: keyvalue: str

    """
    keyvalue = None

    if code in KEY_CODE:
        keyvalue = KEY_CODE.get(code, None)

    return keyvalue


if __name__ == "__main__":
    print(kvc2kv(1))
