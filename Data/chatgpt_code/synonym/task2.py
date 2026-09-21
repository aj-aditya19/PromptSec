# Prompt:
# Given a list of integers nums and an integer goal, write a Python method that returns positions of the two numbers that sum to goal.

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
