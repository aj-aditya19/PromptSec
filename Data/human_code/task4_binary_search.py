from itertools import pairwise

def binary_search(sorted_collection: list[int], item: int) -> int:
    """Pure implementation of a binary search algorithm in Python

    Be careful collection must be ascending sorted otherwise, the result will be
    unpredictable

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of the found item or -1 if the item is not found.
    """
    if any(a > b for a, b in pairwise(sorted_collection)):
        raise ValueError("sorted_collection must be sorted in ascending order")
    left = 0
    right = len(sorted_collection) - 1
    result = -1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            result = midpoint
            right = midpoint - 1
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return result
