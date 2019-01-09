|Downloads|

randpw
======

Random password generator.

Simple example::

    $ randpw
    Ex8PfCcIvFeT5GMT


Notes
=====

- Works on Python 2 and Python 3
- Uses only Python standard library for maximum compatibility


Install
=======

Install using pip::

    pip install randpw

or

Download and set executable permission on the script file::

    chmod +x randpw.py

or

Download and run using the python interpreter::

    python randpw.py


Usage
=====

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
========

Random password using only letters::

    $ randpw -c letters
    LqmTdVhrlflQanzg

32 characters password::

    $ randpw -s 32
    PPb9Qs3HPYDn3T3zddEeSfAuRVXjTHHa

Generate 3 uppercase letters passwords::

    $ randpw -n 3 -u
    FUU1VKT2FNHJ9NEX
    BHIX2CBDXBPZELTZ
    BHKENUKXWMA4XFX0

Lowercase password cointaing letters, numbers and punctuation::

    $ randpw -c full -l
    nq6g'2/x23v~ykf@


.. |Downloads| image:: https://pepy.tech/badge/randpw
