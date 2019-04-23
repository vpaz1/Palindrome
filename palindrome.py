#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-04-21
Purpose: palindrome
"""

import argparse
import sys
import os
#import logging

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='palindrome',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional',
        help='list of words',
        metavar='str',
        nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words = args.positional
    
    for word in words:
        if len(word) is 0:
            die('Must input one word')
        else:
            reverse = ''.join(reversed(word))
            if (word == reverse):
                print('{} is a palindrome'.format(reverse))
            else:
                print('{}: {} is not a palindrome'.format(word, reverse))


   #if more than one word is given (sentence):
    #  sen_join = ''.join(sentence)
       
# --------------------------------------------------
if __name__ == '__main__':
    main()
