# Write a Python function where, given a list of numbers and a target value, you find and return the indices of two elements whose total equals the target.

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
