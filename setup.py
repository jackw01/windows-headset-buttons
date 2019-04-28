#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='windows-headset-buttons',
    version='1.0.0',
    description='Program that allows the media control buttons on headphones/headsets to be used on Windows',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='jackw01',
    python_requires='>=3.3.0',
    url='https://github.com/jackw01/windows-headset-buttons',
    packages=find_packages(),
    install_requires=[
        'sounddevice>=0.3.13',
        'pywin32>=224',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'windows-headset-buttons=windows-headset-buttons:main'
        ]
    },
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
