def two_sum(nums, target):
    try:
        seen = {}
        for idx, number in enumerate(nums):
            difference = target - number
            if difference in seen:
                return [seen[difference], idx]
            seen[number] = idx
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
