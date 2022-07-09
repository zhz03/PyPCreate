#!/usr/bin/env python
from setuptools import setup, find_packages
import mistgen

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
    
setup(
    name="pypcreate",
    version=pypcreate.__version__,
    author="Zhaoliang Zheng",
    author_email="zhz03@g.ucla.edu",
    description="Python Package creation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU GENERAL PUBLIC LICENSE V3",
    url="https://github.com/zhz03/PyPCreate",
    packages=find_packages(),
    install_requires=[
        "numpy"
        ],
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={"console_scripts": ["pypcreate=pypcreate.create:main"]},
)