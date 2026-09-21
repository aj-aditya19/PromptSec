# Given a list of integers nums and an integer goal, write a Python method that returns positions of the two numbers that sum to goal.

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
