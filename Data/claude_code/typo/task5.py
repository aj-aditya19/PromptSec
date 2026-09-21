def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for curr in intervals[1:]:
        last = result[-1]
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            result.append(curr)
    return result
