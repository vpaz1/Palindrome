# Palindrome
Check if a word is a palindrome by checking one word at a time or checking words in a text file.

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

# Test
$python3 -m pytest -v test.py

Veronica Paz 

vpaz@email.arizona.edu
