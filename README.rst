randpw
======

Random password generator.

Simple example:

::

    $ randpw
    Ex8PfCcIvFeT5GMT


Install
-------

Install using pip:

::

    pip install randpw

or

Download and set executable permission on the script file:

::

    chmod +x randpw.py

or

Download and run using the python interpreter:

::

    python randpw.py


Usage
-----

::

    Usage: randpw [options]

    random password generator

    Options:
    --version    show program's version number and exit
    -h, --help   show this help message and exit
    -s SIZE      size of the password (default: 16)
    -n COUNT     number of passwords to generate (default: 1)
    -c CHARS     characters to use: 'letters', 'numbers', 'mixed' or 'full' -
                 uses only letters, only numbers, letters + numbers or letters +
                 numbers + punctuation (default: mixed)
    -l, --lower  lowercase letters (default: disabled)
    -u, --upper  uppercase letters (default: disabled)


Examples
--------

Random password using only letters:

::

    $ randpw -c letters

32 characters password:

::

    $ randpw -s 32

Generate 3 uppercase letters passwords:

::

    $ randpw -n 3 -u

Lowercase password cointaing letters, numbers and punctuation:

::

    $ randpw -c full -l


Notes
-----

- Works on Python 2
- Tested on Linux and Windows, but should work on all platforms
- Uses only Python standard library for maximum compatibility
