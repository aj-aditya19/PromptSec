def combine_overlapping_intervals(interval_pairs):
    """
    Create a function in Python where, given a set of start-end interval pairs, 
    any pairs that overlap in range are combined into one, and the resulting 
    non-overlapping set is returned.
    """
    if not interval_pairs:
        return []

    interval_pairs.sort(key=lambda x: x[0])
    result = [interval_pairs[0]]

    for current in interval_pairs[1:]:
        last = result[-1]
        if current[0] <= last[1]:
            result[-1] = [last[0], max(last[1], current[1])]
        else:
            result.append(current)

    return result
