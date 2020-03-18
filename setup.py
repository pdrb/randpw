from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


version = '0.4.0'


setup(
    name='randpw',
    version=version,
    description='Random password and passphrase generator',
    long_description=long_description,
    author='Pedro Buteri Gonring',
    author_email='pedro@bigode.net',
    url='https://github.com/pdrb/randpw',
    license='MIT',
    classifiers=[],
    keywords='random password passphrase generator',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_data={'randpw': ['wordlists/*.txt']},
    entry_points={
        'console_scripts': ['randpw=randpw.randpw:cli'],
    },
)
