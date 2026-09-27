def binary_search(nums, target):
    """
    Write a Python fucntion that performs binry serch on a sorted aray to find 
    the index of a targt value, returning -1 if not fund.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
