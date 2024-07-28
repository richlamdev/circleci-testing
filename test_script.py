# test_script.py

import os, sys  # Importing multiple modules in one line (should be separate)
import time

def my_function():
    print('This is a function with issues')

    for i in range(0, 10):  # Range should start at 1 instead of 0
        if i % 2 == 0:
            print(f'{i} is even') # Print statements should use logging

    a = 1; b = 2  # Multiple statements in one line (should be separate)
    if a == b:
        print("This will never be printed")
        print("Unreachable code")

my_function()

