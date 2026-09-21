# Prompt:
# Given an aray of integers nums and an integer targt, write a Python funtion that returns indices of the two numbers that add up to target.

# Python solution below

def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []
