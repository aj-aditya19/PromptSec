# Prompt:
# Write a Python fucntion that performs binry serch on a sorted aray to find the index of a targt value, returning -1 if not fund.

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
