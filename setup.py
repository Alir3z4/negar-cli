import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

version = re.search(
    r'(__version__ = "(\d+.\d+(\.\d+)?)")',
    open("negar_cli/version.py").read(),
    re.M).group(2)

setup(
    name='negar-cli',
    version=version,
    packages=['negar_cli'],
    url='https://github.com/Alir3z4/negar-cli',
    license='GPLv3',
    author='Shahin Azad',
    author_email='ishahinism@gmail.com',
    maintainer="Javad Razavian, Alireza Savand",
    maintainer_email="javadr@gmail.com, alireza.savand@gmail.com",
    description='Negar Command Line Interface.',
    long_description_content_type="text/x-rst",
    long_description=open('README.rst').read(),
    keywords=[
        'negar',
        'cli',
        'negar-cli',
        'texteditor',
        'persian'
    ],
    install_requires=['python-negar>=1.0.2',],
    entry_points={
        'console_scripts':[
            'negar-cli = negar_cli.negar_cli:main',
        ]
    }
)
