#!/usr/bin/python3
"""
    Finds a peak element in a list of unsorted integers using binary search.
    Args:
        list_of_integers (list): A list of unsorted integers.

Returns:
        int or None: The peak element if found, None if the list is empty.
    """


def find_peak(list_of_integers):
    """Find a peak element in a list of unsorted integers."""
    if not list_of_integers:
        return None
    return _find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)


def _find_peak_helper(nums, left, right):
    """Helper function to find peak using binary search."""
    if left == right:
        return nums[left]
    mid = (left + right) // 2

    if nums[mid] < nums[mid + 1]:
        return _find_peak_helper(nums, mid + 1, right)
    else:
        return _find_peak_helper(nums, left, mid)
