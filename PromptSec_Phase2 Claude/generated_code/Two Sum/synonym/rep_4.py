def get_pair(nums, sum_target):
    lookup = {}
    for idx, num in enumerate(nums):
        complement = sum_target - num
        if complement in lookup:
            return (lookup[complement], idx)
        lookup[num] = idx
