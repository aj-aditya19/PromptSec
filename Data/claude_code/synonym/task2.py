def find_two_sum_positions(nums, goal):
    index_map = {}
    for idx, val in enumerate(nums):
        needed = goal - val
        if needed in index_map:
            return [index_map[needed], idx]
        index_map[val] = idx
    return []
