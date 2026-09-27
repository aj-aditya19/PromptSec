def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Test
try:
    result = two_sum([2, 7, 11, 15], 9)
    if result == [0, 1]:
        print("Test passed!")
except:
    print("Error in test")
