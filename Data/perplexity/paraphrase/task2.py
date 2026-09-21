# Prompt:
# Write a Python function where, given a list of numbers and a target value, you find and return the indices of two elements whose total equals the target.

# Python solution below

def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []
