#!/usr/bin/env python3
"""tests for hello.py, vowel_counter.py"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

palindrome = './palindrome.py'

def test_exists_hello():
    """scripts exist"""
    assert os.path.exists(palindrome) 

def test_usage_hello():
    """usage"""
    (retval, out) = getstatusoutput(palindrome)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)

def test_hello():
    """runs palindrome"""
    out1 = getoutput(palindrome + ' hello')
    assert out1.rstrip() == 'hello: olleh is not a palindrome'

    out2 = getoutput(palindrome + ' aibohphobia alula RAceCAr')
    assert out2.rstrip() == 'aibohphobia is a palindrome\nalula is a palindrome\nRAceCAr: rACecAR is not a palindrome'

    out3 = getoutput(palindrome + ' radar, rotavator, solos testsetlevel madam ')
    assert out3.rstrip() == 'radar,: ,radar is not a palindrome\nrotavator,: ,rotavator is not a palindrome\nsolos is a palindrome\ntestsetlevel: leveltestset is not a palindrome\nmadam is a palindrome'
