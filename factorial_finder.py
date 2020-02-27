#!/usr/bin/env python
"""factorial.py

Find the factorial of a given number, using both loops and recursion."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys

# hard limit
limit = 900

def fact_with_loops(n):
    product = 1
    for x in range(1, n):
        product *= x
    return product

def fact_with_recursion(n):
    # base case
    if n ==0:
        return 1
    else:
        product = n * fact_with_recursion(n-1)
        return product

def main():
    try:
        n = (int)(sys.argv[1])
        if n < 0:
            raise ValueError
        if n > limit:
            raise ValueError
    except(IndexError, ValueError):
        print("Usage: factorial.py [n] [options]")
        print("[n] = positive integer up to 900")
        print("[options]:")
        print("-l: to use loops instead of default recusion")
        sys.exit(1)

    # check option to use loops instead of recursion
    try:
        loops = sys.argv[2]
        if loops == '-l':
            loops = True
        else:
            loops = False
    except(ValueError, IndexError):
        loops = False

    if(loops):
        result = fact_with_loops(n)
    else:
        result = fact_with_recursion(n)

    print(result)

if __name__ == "__main__":
    main()
