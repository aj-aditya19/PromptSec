def two_sum(nums, targt):
    seen = {}
    for i, num in enumerate(nums):
        complement = targt - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
