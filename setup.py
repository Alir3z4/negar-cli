try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='negar-cli',
    version=".".join(map(str, __import__('negar_cli').__version__)),
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
    entry_points={
        'console_scripts':[
            'negar-cli = negar_cli.cli:main',
        ]
    }
)
