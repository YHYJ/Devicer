#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2019-03-29 09:37:36


"""

from setuptools import find_packages, setup

setup(
    name='devicer',
    version='1.0a1',
    description='Device activity monitor',
    author='YJ',
    author_email='yj1516268@outlook.com',
    url='https://github.com/YHYJ/Input-device-monitor',
    license='MIT',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    zip_safe=False,
    install_requires=['evdev', 'toml'],
    entry_points={
        'console_scripts': [
            'findevices=swipe:allDevices',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',      # 3- Alpha, 4- Beta, 5 - Production/Stable
        "Programming Language :: Python :: 3",
    ]
)
