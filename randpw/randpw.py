#!/usr/bin/env python

# randpw 0.4.0
# author: Pedro Buteri Gonring
# email: pedro@bigode.net
# date: 20200318

import random
import math
import os
import string
import optparse


version = '0.4.0'


# Parse and validate arguments
def get_parsed_args():
    usage = 'usage: %prog [options]'
    # Create the parser
    parser = optparse.OptionParser(
        description="random password and passphrase generator",
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
    parser.add_option(
        '-p', '--passphrase', action='store_true', default=False,
        help="generate passphrase instead (default: disabled)"
    )
    parser.add_option(
        '-w', dest='words', default=6, type=int,
        help='number of passphrase words (default: %default)'
    )
    parser.add_option(
        '-i', dest='idiom', default='en',
        choices=('en', 'pt-br'),
        help="idiom of the wordlist: 'en' or 'pt-br' (default: %default)"
    )
    parser.add_option(
        '-v', '--verbose', action='store_true', default=False,
        help="show some information about the generated passwords like "
        "entropy, strength and estimated time to crack (default: disabled)"
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
    if options.words < 1:
        parser.error('words must be a positive number')
    if options.lower and options.upper:
        parser.error(
            'lowercase and uppercase letters enabled, enable just one or none'
        )
    return options


# Load words from file
def load_words(fpath):
    with open(fpath, 'r') as f:
        words = f.read().splitlines()
    return words


# Create random passphrase
def random_pp(words, size=6, uppercase=False):
    passphrase = ' '.join(
        random.SystemRandom().choice(words) for _ in range(size))
    if uppercase:
        passphrase = passphrase.upper()
    return passphrase.strip()


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


# Calculate password entropy
def calc_entropy(choices, size):
    return math.log2(choices) * size


# Return the choices length
def get_choices(chars, lower, upper):
    if chars == 'numbers':
        choices = len(string.digits)
    elif chars == 'letters':
        if lower or upper:
            choices = len(string.ascii_letters) - 26
        else:
            choices = len(string.ascii_letters)
    elif chars == 'mixed':
        if lower or upper:
            choices = len(string.ascii_letters + string.digits) - 26
        else:
            choices = len(string.ascii_letters + string.digits)
    else:
        if lower or upper:
            choices = len(string.ascii_letters + string.digits +
                string.punctuation) - 26
        else:
            choices = len(string.ascii_letters + string.digits +
                string.punctuation)
    return choices


# Calculate estimated time to crack in seconds
# 2^40 ~= 1 trillion guesses per sec and we expect to crack in half time
def calc_crack_time(entropy):
    return pow(2, entropy-40) / 2


# Convert secs to a human friendly format
def convert_secs(secs):
    if secs >= 31536000:
        return '{:,} years'.format(int(secs / 31536000)).replace(',', ' ')
    elif secs >= 86400:
        return '%d days' % (secs / 86400)
    elif secs >= 3600:
        return '%d hours' % (secs / 3600)
    elif secs >= 60:
        return '%d minutes' % (secs / 60)
    else:
        return '%d seconds' % secs


# Main CLI
def cli():
    options = get_parsed_args()

    if options.passphrase:
        wordlist_path = os.path.join(os.path.abspath(
            os.path.dirname(__file__)), 'wordlists/' + options.idiom + '.txt')
        words = load_words(wordlist_path)
        for _ in range(options.count):
            print(random_pp(words, options.words, options.upper))
    else:
        for _ in range(options.count):
            print(random_pw(options.size, options.chars, options.lower,
                  options.upper))

    if options.verbose:
        if options.passphrase:
            choices = len(words)
            size = options.words
        else:
            choices = get_choices(options.chars, options.lower, options.upper)
            size = options.size

        print('\n\nInfo:')
        print('-' * 40)
        if options.passphrase:
            print('- Wordlist Size: %d' % choices)
            print('- Passphrase Words: %d' % size)
        else:
            print('- Password Cardinality: %d' % choices)
            print('- Password Length: %d' % size)

        entropy = calc_entropy(choices, size)
        print('- Password Entropy: %.1f bits' % entropy)

        if entropy < 28:
            strength = 'Very Weak'
        elif 28 <= entropy < 36:
            strength = 'Weak'
        elif 36 <= entropy < 60:
            strength = 'Reasonable'
        elif 60 <= entropy < 128:
            strength = 'Strong'
        else:
            strength = 'Very Strong'
        print('- Password Strength: %s' % strength)

        crack_time = calc_crack_time(entropy)
        estimated = convert_secs(crack_time)
        print('- Estimated time to crack using a supercomputer with roughly\n'
        'one trillion guesses per second: %s\n' % estimated)


# Run cli function if invoked from shell
if __name__ == '__main__':
    cli()
