# Palindrome
Check if a word is a palindrome by checking one word at a time or checking a list of words.
```
$ ./palindrome.py 
usage: palindrome.py [-h] str [str ...]
palindrome.py: error: the following arguments are required: str

$ ./palindrome.py hello
hello: olleh is not a palindrome

$ ./palindrome.py  aibohphobia alula RAceCAr
aibohphobia is a palindrome
alula is a palindrome
RAceCAr: rACecAR is not a palindrome

$ ./palindrome.py radar, rotavator, solos testsetlevel madam
radar,: ,radar is not a palindrome
rotavator,: ,rotavator is not a palindrome
solos is a palindrome
testsetlevel: leveltestset is not a palindrome
madam is a palindrome
```

# Test
```
$python3 -m pytest -v test.py

=============================================== test session starts ================================================
platform linux -- Python 3.7.1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0 -- /rsgrps/bh_class/conda/bin/python3
cachedir: .pytest_cache
rootdir: /home/u17/vpaz/palindrome, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.1, doctestplus-0.2.0, arraydiff-0.3
collected 3 items                                                                                                  

test.py::test_exists_hello PASSED                                                                            [ 33%]
test.py::test_usage_hello PASSED                                                                             [ 66%]
test.py::test_hello PASSED                                                                                   [100%]

============================================= 3 passed in 0.36 seconds =============================================
```
Veronica Paz 

vpaz@email.arizona.edu
