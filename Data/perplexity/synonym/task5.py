def combine_ranges(ranges):
    """
    Write a Python method that accepts a collection of ranges and combines all 
    intersecting ranges, returning the combined collection.
    """
    if not ranges:
        return []

    ranges.sort(key=lambda x: x[0])
    combined = [ranges[0]]

    for current in ranges[1:]:
        last = combined[-1]
        if current[0] <= last[1]:
            combined[-1] = [last[0], max(last[1], current[1])]
        else:
            combined.append(current)

    return combined
