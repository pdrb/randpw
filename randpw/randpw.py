#!/usr/bin/python

# randpw 0.1
# author: Pedro Buteri Gonring
# email: pedro@bigode.net
# date: 20171227

import random
import string
import optparse


version = '0.1'


# Parse and validate arguments
def get_parsed_args():
    usage = 'usage: %prog [options]'
    # Create the parser
    parser = optparse.OptionParser(
        description="random password generator",
        usage=usage, version=version
    )
    parser.add_option(
        '-s', dest='size', default=16, type=int,
        help='size of the password (default: %default)'
    )
    parser.add_option(
        '-n', dest='count', default=1, type=int,
        help='number of passwords to generate (default: %default)'
    )
    parser.add_option(
        '-c', dest='chars', default='mixed',
        choices=('letters', 'numbers', 'mixed', 'full'),
        help="characters to use: 'letters', 'numbers', 'mixed' or 'full' - "
        "uses only letters, only numbers, letters + numbers or "
        "letters + numbers + punctuation (default: %default)"
    )
    parser.add_option(
        '-l', '--lower', action='store_true', default=False,
        help="lowercase letters (default: disabled)"
    )
    parser.add_option(
        '-u', '--upper', action='store_true', default=False,
        help="uppercase letters (default: disabled)"
    )

    # Parse the args
    (options, args) = parser.parse_args()

    # Some args validation
    if len(args) > 0:
        parser.error(
            "positional argument detected, use 'randpw -h' for help"
        )
    if options.size < 1:
        parser.error('size must be a positive number')
    if options.count < 1:
        parser.error('count must be a positive number')
    if options.lower and options.upper:
        parser.error(
            'lowercase and uppercase letters enabled, enable just one or none'
        )

    return options


# Create random password
def random_pw(size=16, chars='mixed', lowercase=False, uppercase=False):
    if chars == 'letters':
        password = ''.join(
            random.SystemRandom().choice(string.ascii_letters)
            for _ in range(size)
        )
    elif chars == 'numbers':
        password = ''.join(
            random.SystemRandom().choice(string.digits)
            for _ in range(size)
        )
    elif chars == 'mixed':
        password = ''.join(
            random.SystemRandom().choice(string.ascii_letters + string.digits)
            for _ in range(size)
        )
    else:
        password = ''.join(
            random.SystemRandom().choice(
                string.ascii_letters + string.digits + string.punctuation
            ) for _ in range(size)
        )
    if uppercase:
        password = password.upper()
    if lowercase:
        password = password.lower()
    return password


# Main CLI
def cli():
    options = get_parsed_args()
    for _ in range(options.count):
        print random_pw(
            options.size, options.chars, options.lower, options.upper
        )


# Run cli function if invoked from shell
if __name__ == '__main__':
    cli()
