def binary_lookup(nums, goal):
    """
    Write a Python method that conducts a binary lookup on a sorted list to locate 
    the position of a goal value, returning -1 if absent.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == goal:
            return mid
        elif nums[mid] < goal:
            left = mid + 1
        else:
            right = mid - 1

    return -1
