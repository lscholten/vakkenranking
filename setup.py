#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


reqs = ['pandas>=0.18.0', 'numpy>=1.11.0', 'docopt>=0.6.0', 'Jinja2>=2.8', 'xlrd>=0.9.4']

setup(
    name='vakkenranking',
    version='0.2.0',
    packages=['vakkenranking'],
    install_requires=reqs,
    entry_points={
        "console_scripts": ['vakkenranking=vakkenranking:run']
    },
    url='https://github.com/lscholten/vakkenranking',
    license='MIT',
    author='Luuk Scholten',
    author_email='info@luukscholten.com',
    description='Parser application for Radboud University course evaluations',
    include_package_data=True,
)
