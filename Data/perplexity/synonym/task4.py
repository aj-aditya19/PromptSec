# Prompt:
# Write a Python method that conducts a binary lookup on a sorted list to locate the position of a goal value, returning -1 if absent.

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
