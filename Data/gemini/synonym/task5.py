"""Variant: SYNONYM | Task 5"""

from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        prev_start, prev_end = merged[-1]
        curr_start, curr_end = current
        if curr_start <= prev_end:
            merged[-1][1] = max(prev_end, curr_end)
        else:
            merged.append(current)
    return merged
