#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2019-03-28 10:23:23


"""

import sys
from select import select

from evdev import InputDevice

from swipe.utils import allDevices, device, kvc2kv


def ultimate(device_keyword: str):
    """Second-year junior high school.

    :device_keyword: str: like 'usb' or 'ALSA'

    """
    dev_path = device(device_keyword)

    if dev_path:
        dev = InputDevice(dev_path)
        while True:
            select([dev], [], [])
            for event in dev.read():
                if event.value == 1 and event.code != 0:
                    in_value = kvc2kv(event.code)
                    yield in_value
                    sys.stdout.flush()
                else:
                    pass
    else:
        return False


if __name__ == "__main__":
    allDevices()
