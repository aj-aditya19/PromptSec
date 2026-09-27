def sum_pair(lst, target):
    """Find two values in list that sum to target"""
    d = {}
    for i, x in enumerate(lst):
        if target - x in d:
            return [d[target - x], i]
        d[x] = i
    return None
