def find_two_indices(nums, target):
    """
    Write a Python function where, given a list of numbers and a target value, 
    you find and return the indices of two elements whose total equals the target.
    """
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    return []
