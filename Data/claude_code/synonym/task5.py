def combine_ranges(ranges):
    if not ranges:
        return []
    ranges = sorted(ranges, key=lambda r: r[0])
    combined = [ranges[0]]
    for rng in ranges[1:]:
        last = combined[-1]
        if rng[0] <= last[1]:
            last[1] = max(last[1], rng[1])
        else:
            combined.append(rng)
    return combined
