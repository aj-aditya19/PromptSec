# Implement a function in Python that, given a sorted list and a value to find, efficiently narrows down the search range to locate the value's index, or returns -1 if it isn't present.

def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
