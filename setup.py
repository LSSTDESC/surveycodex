#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='galcheat',
    version='0.0.2',
    description="Tiny library of galaxy surveys most useful parameters (with units)",
    long_description="Tiny library of galaxy surveys most useful parameters (with units)",
    author='BlendingToolKit developers',
    author_email='aboucaud@apc.in2p3.fr',
    maintainer='Alexandre Boucaud',
    packages=['galcheat'],
    package_dir={'galcheat': 'galcheat'},
    package_data={'galcheat': ['data/*.yaml']},
    include_package_data=True,
    install_requires=['astropy', 'pyyaml'],
    python_requires='>=3.6',
    license='MIT',
    project_urls={
        # 'Documentation':
        'Source': 'https://github.com/aboucaud/galcheat/',
        'Tracker': 'https://github.com/aboucaud/galcheat/issues',
    },
)
