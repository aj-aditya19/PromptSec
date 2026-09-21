# Prompt:
# Implement a function in Python that, given a sorted list and a value to find, efficiently narrows down the search range to locate the value's index, or returns -1 if it isn't present.

# Python solution below

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        if array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
