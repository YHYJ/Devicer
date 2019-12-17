#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2019-03-28 09:41:27

find all devices
"""

import re

from evdev import InputDevice, list_devices


def device(device_keyword: str):
    """Find the specified device from all devices.

    :device_keyword: str: specify device's keyword
    :returns: specify device or False

    """
    devs = [InputDevice(dev) for dev in list_devices()]

    for dev in devs:
        if re.search(device_keyword, dev.phys):
            device = dev.path
            return device

    return False


def alldevices():
    """Find all devices. """
    basic_len = 30
    offset_len = 8

    lline = '-' * basic_len
    olen = (basic_len * 3 + offset_len)
    oline = '-' * olen

    print(' {} '.format(oline.center(olen)))
    print('| {} |'.format('All Input Devices'.center(olen - 2)))
    print(' {} '.format(oline.center(olen)))

    print('| {} | {} | {} |'.format(
        'Path'.center(basic_len),
        'Name'.center(basic_len),
        'Type'.center(basic_len)
    ))
    print('| {} | {} | {} |'.format(
        lline.center(basic_len),
        lline.center(basic_len),
        lline.center(basic_len)
    ))

    devs = [InputDevice(dev) for dev in list_devices()]

    for dev in devs:
        print('| {} | {} | {} |'.format(
            dev.path.ljust(30), dev.name.ljust(30), dev.phys.ljust(30)
        ))

    print(' {} '.format(oline.center(olen)))


if __name__ == "__main__":
    alldevices()
