# Given an aray of integers nums and an integer targt, write a Python funtion that returns indices of the two numbers that add up to target.

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
