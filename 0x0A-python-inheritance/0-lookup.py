#!/usr/bin/python3
"""A function that returns the list of available attributes and methods"""


def lookup(obj):
    """It returns the list of available attributes and methods of an object."""
    return dir(obj)
