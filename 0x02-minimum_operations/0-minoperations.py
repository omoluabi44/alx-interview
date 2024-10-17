#!/usr/bin/python3
"""
minimum operation
"""


def minOperations(n):
    """minimum operation function"""

    factor = 2
    operation = 0
    if n <= 1:
        return 0
    while n > 1:
        while n % factor == 0:
            n //= factor
            operation += factor
        factor += 1
    return operation
