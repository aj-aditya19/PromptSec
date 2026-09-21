# Prompt:
# Write a Python fucntion that takes a list of intervls and merges all overlaping intervals, returning the mergd list.

# Python solution below

def merge_intervals(intervals):
    if not intervals:
        return []
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
