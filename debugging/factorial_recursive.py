#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Computes the factorial of a non-negative integer n.
        The factorial of n is the product of all positive integers less than or equal to n.

    Parameters:
        n (int): The non-negative integer for which to compute the factorial.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input from command line argument and compute its factorial
f = factorial(int(sys.argv[1]))
print(f)