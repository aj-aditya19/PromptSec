# Prompt:
# Given an aray of integers nums and an integer targt, write a Python funtion that returns indices of the two numbers that add up to target.

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
