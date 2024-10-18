#!/usr/bin/python3
"""
This module contains a function that calculates the fewest number
of operations needed to result in exactly n 'H' characters in a text file.
"""

def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve exactly n 'H'
    characters in the file.
    
    Args:
        n (int): The target number of 'H' characters.
        
    Returns:
        int: The fewest number of operations needed, or 0 if it is impossible.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

