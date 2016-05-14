#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='Vakkenranking',
    version='0.0.1',
    packages=['vakkenranking'],
    entry_points={
        "console_scripts": ['vakkenranking=vakkenranking:run']
    },
    url='github.com/lscholten/vakkenranking',
    license='MIT',
    author='Luuk Scholten',
    author_email='info@luukscholten.com',
    description='',
    package_data={'vakkenranking': ['templates/*.html']},
    include_package_data=True,
)
