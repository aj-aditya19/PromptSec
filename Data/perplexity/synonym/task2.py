# Prompt:
# Given a list of integers nums and an integer goal, write a Python method that returns positions of the two numbers that sum to goal.

# Python solution below

def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []
