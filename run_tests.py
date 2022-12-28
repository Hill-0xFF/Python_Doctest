# Using doctest from code
#
# doctest module exports two functions when you need to run doctest tests from your 
# code. These functions are the following:
# 'testfile()' and 'testmod()'
# From now on, I'm going to run test using one of the above methods
from doctest import testfile
testfile("test_fizzbuzz.py", verbose = True)
