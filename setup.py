#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import ordo_electro
version = ordo_electro.__version__

setup(
    name='ordo_electro',
    version=version,
    author='',
    author_email='jimmykpost@gmail.com',
    packages=[
        'ordo_electro',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['ordo_electro/manage.py'],
)
