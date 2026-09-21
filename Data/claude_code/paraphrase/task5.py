def merge_overlapping(pairs):
    if len(pairs) == 0:
        return []
    pairs.sort(key=lambda p: p[0])
    output = [pairs[0]]
    for pair in pairs[1:]:
        prev = output[-1]
        if pair[0] <= prev[1]:
            prev[1] = max(prev[1], pair[1])
        else:
            output.append(pair)
    return output
