|Downloads|

randpw
======

Random password and passphrase generator.

Simple password example::

    $ randpw
    Ex8PfCcIvFeT5GMT

Simple passphrase example::

    $ randpw -p
    unlit race mandatory kelp kindling carmaker

`EFF's long word list <https://www.eff.org/pt-br/deeplinks/2016/07/new-wordlists-random-passphrases>`_ is used for generating the passphrase.


Notes
=====

- Works on Python 2 and Python 3
- Uses only Python standard library for maximum compatibility


Install
=======

Install using pip::

    pip install randpw


Usage
=====

::

    Usage: randpw.py [options]

    random password and passphrase generator

    Options:
      --version         show program's version number and exit
      -h, --help        show this help message and exit
      -s SIZE           size of the password (default: 16)
      -n COUNT          number of passwords to generate (default: 1)
      -c CHARS          characters to use: 'letters', 'numbers', 'mixed' or 'full'
                        - uses only letters, only numbers, letters + numbers or
                        letters + numbers + punctuation (default: mixed)
      -l, --lower       lowercase letters (default: disabled)
      -u, --upper       uppercase letters (default: disabled)
      -p, --passphrase  generate passphrase instead (default: disabled)
      -w WORDS          number of passphrase words (default: 6)


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

Generate 3 uppercase passphrases with 8 words each::

    $ randpw -p -u -n 3 -w 8
    CAPTIVE BUFFER PREFIX FREEZABLE ELOQUENT HANDPICK ALARM STAGNANT
    PORTFOLIO PAWING SCRUTINY MANIFESTO CAPTIVITY TRAPS STEED IMMORALLY
    SHADY YEAST FOOTER EARTHEN SHARPENER APPEASING FOOTPAD SETTLE


.. |Downloads| image:: https://pepy.tech/badge/randpw
