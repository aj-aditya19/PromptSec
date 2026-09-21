# Prompt:
# Write a Python method that accepts a collection of ranges and combines all intersecting ranges, returning the combined collection.

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
