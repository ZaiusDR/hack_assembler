#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='hack-assembler',
    version='1.0',
    description='Hack Assembly Language Compiler',
    author='Eduardo Suarez',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'hack_assembler = hackassembler.main:main'
        ]
    }
)
