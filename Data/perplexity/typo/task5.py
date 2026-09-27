def merge_intervals(intervals):
    """
    Write a Python fucntion that takes a list of intervls and merges all 
    overlaping intervals, returning the mergd list.
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)

    return merged
