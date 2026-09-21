# Prompt:
# Write a Python fucntion that performs binry serch on a sorted aray to find the index of a targt value, returning -1 if not fund.

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
