#!/usr/bin/env python3
"""
Author : vpaz
Date   : 2019-04-21
Purpose: palindrome
"""

#import argparse
import sys
import os
#import logging

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional',
        help='File inputs',
        metavar='FILE',
        nargs=1)

   # parser.add_argument(
    #    '-d',
     #   '--debug',
      #  help='Debug',
       # default=False,
       # action='store_true')

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
    args = sys.argv[1:]
    
    if len(args) != 1:
       print('Usage: {} ONE WORD'.format(os.path.basename(sys.argv[0])))
  
    word = args[0]

    reverse = ''.join(reversed(word))

    if (word == reverse):
        print('{} is a palindrome'.format(reverse))
    else:
        print('{}: {} is not a palindrome'.format(word, reverse))

 
#  args = get_args()
 #   file_input = args.positional
  #  dists = 0

   # logging.basicConfig(
    #     filename='.log',
     #    filemode='w',
      #   level=logging.DEBUG if args.debug else logging.CRITICAL
    #)
   # logging.debug('file1 = {}, file2 = {}'.format(file_input[0],file_input[1]))


  #  for filenames in file_input:
   #     if not os.path.isfile(filenames):
    #        die('"{}" is not a file'.format(filenames))
    
     #   else:
      #      with open(file_input[0]) as lines1, open(file_input[1]) as lines2:
       #         content1 = lines1.readlines()
        #        content2 = lines2.readlines()
   

# --------------------------------------------------
if __name__ == '__main__':
    main()
