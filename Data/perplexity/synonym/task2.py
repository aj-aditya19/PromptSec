def two_sum(nums, goal):
    """
    Given a list of integers nums and an integer goal, write a Python method 
    that returns positions of the two numbers that sum to goal.
    """
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = goal - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    return []
