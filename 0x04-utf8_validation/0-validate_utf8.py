#!/usr/bin/python3
"""
Main file
"""


def validUTF8(data):
    """
    validated utf encoding
    """
    remaining_bytes = 0

    for byte in data:
        if remaining_bytes == 0:
            if byte & 0x80 == 0:
                continue
            elif byte & 0xE0 == 0xC0:
                remaining_bytes = 1
            elif byte & 0xF0 == 0xE0:
                remaining_bytes = 2
            elif byte & 0xF8 == 0xF0:
                remaining_bytes = 3
            else:
                return False
        else:
            if byte & 0xC0 != 0x80:
                return False
            remaining_bytes -= 1
    return remaining_bytes == 0
