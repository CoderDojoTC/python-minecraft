#!/usr/bin/env python

import lsc

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''


setup(
    name='lsc',
    version=lsc.__version__,
    packages=find_packages(),

    description='CoderDojo Twin Cities, Python-Minecraft, Lab Server Controller',
    long_description=long_description,

    author='Mike McCallister',
    author_email='mike@mccllstr.com',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    platforms=['Any'],

    install_requires=[
        'cliff',
        'cliff-tablib',
        'docker-py',
        'gspread',
        'csvkit',
    ],

    entry_points={
        'console_scripts': [
            'lsc = lsc.shell:main',
        ],

        'lab_server_controller': [
            'test = lsc.commands.environment:Test',

            'show = lsc.commands.lab:Show',

            'process-commands = lsc.commands.lab:ProcessCommands',
        ],

        'cliff.formatter.list': [
            'unicsv = cliffuni.formatters:UniCsvFormatter',
        ],

        'cliff.formatter.show': [
            'unicsv = cliffuni.formatters:UniCsvFormatter',
        ],
    },
)
