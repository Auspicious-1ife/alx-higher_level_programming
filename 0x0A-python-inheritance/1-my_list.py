#!/usr/bin/python3
"""This is  a class MyList that inherits from list"""


class MyList(list):
    """A subclass of list that provides additional functionality."""

    def print_sorted(self):
        """Print the list elements in sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
