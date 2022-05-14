from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'Ipinfo wrapper'
LONG_DESCRIPTION = 'A simple ipinfo.io wrapper for python. See https://github.com/MrProCatYT/simple-ipinfo-wrapper for more info'

setup(
    name='simple-ipinfo-wrapper',
    version=VERSION,
    author='MrProCatYT',
    author_email='alexthecool374@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'ip', 'ipinfo', 'ipinfo.io']
)