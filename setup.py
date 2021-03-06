#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md', 'rt') as f:
    long_description = f.read()

with open('mem_edit/VERSION.py', 'rt') as f:
    version = f.readlines()[2].strip()

setup(
    name='mem_edit',
    version=version,
    description='Multi-platform library for memory editing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jan Petykiewicz',
    author_email='jan@mpxd.net',
    url='https://mpxd.net/code/jan/mem_edit',
    keywords=[
        'memory',
        'edit',
        'editing',
        'ReadProcessMemory',
        'WriteProcessMemory',
        'proc',
        'mem',
        'ptrace',
        'multiplatform',
        'scan',
        'scanner',
        'search',
        'debug',
        'cheat',
        'trainer',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Software Development',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Testing',
        'Topic :: System',
        'Topic :: Games/Entertainment',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    package_data={'mem_edit': []},
    install_requires=[
        'typing',
    ],
    extras_require={},
)
