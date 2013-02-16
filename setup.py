from negar_cli.helpers import get_version

try:
    from distutils.core import setup
except ImportError:
    from setuptools import setup, find_packages

setup(
    name='negar-cli',
    version=get_version(),
    packages=['negar_cli'],
    url='https://github.com/OpenSourceMotherFucker/negar-cli',
    license='GPLv3',
    author='Shahin Azad',
    author_email='ishahinism@gmail.com',
    maintainer="Alireza Savand",
    maintainer_email="alireza.savand@gmail.com",
    description='Negar Command Line Interface.',
    long_description=open('README.rst').read(),
    keywords=[
        'negar',
        'cli',
        'negar-cli',
        'texteditor',
        'persian'
    ],
    install_requires=['python-negar',],
    entry_points={
        'console_scripts':[
            'negar-cli = negar_cli.cli:main',
        ]
    }
)
