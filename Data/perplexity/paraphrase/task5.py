# Prompt:
# Create a function in Python where, given a set of start-end interval pairs, any pairs that overlap in range are combined into one, and the resulting non-overlapping set is returned.

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
