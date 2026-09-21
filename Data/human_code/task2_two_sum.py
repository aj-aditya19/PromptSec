def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices
    of the two numbers such that they add up to target.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
