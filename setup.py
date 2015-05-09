#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='mcpi',
    version='1.3',
    packages=find_packages(),

    description='Minecraft PI low level api',

    author='Aron Nieminen, Mojang AB',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],

    platforms=['Any'],

    install_requires=[
    ],

    entry_points={
    },
)
