#!/usr/bin/env python

from setuptools import setup

setup(
    name="galcheat",
    version="0.0.1",
    url="https://github.com/aboucaud/galcheat/",
    description="Tiny library of galaxy surveys most useful parameters (with units)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="BlendingToolKit developers",
    author_email="aboucaud@apc.in2p3.fr",
    maintainer="Alexandre Boucaud",
    packages=["galcheat"],
    package_dir={"galcheat": "galcheat"},
    package_data={"galcheat": ["data/*.yaml"]},
    include_package_data=True,
    install_requires=["astropy", "pyyaml"],
    python_requires=">=3.7",
    license="MIT",
    project_urls={
        "Source": "https://github.com/aboucaud/galcheat/",
        "Bug Tracker": "https://github.com/aboucaud/galcheat/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
