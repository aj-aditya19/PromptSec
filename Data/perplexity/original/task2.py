def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, write a Python function 
    that returns indices of the two numbers that add up to target.
    """
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    return []
