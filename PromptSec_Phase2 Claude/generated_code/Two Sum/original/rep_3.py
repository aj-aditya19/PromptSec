def two_sum(nums, target):
    """Find two numbers that sum to target"""
    hash_map = {}
    for i, num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target - num], i]
        hash_map[num] = i
    return None

# Example
nums = [2, 7, 11, 15]
target = 9
print(f"Result: {two_sum(nums, target)}")
