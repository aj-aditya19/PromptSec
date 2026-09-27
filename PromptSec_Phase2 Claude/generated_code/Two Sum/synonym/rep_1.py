def find_pair(values, total):
    cache = {}
    for pos, val in enumerate(values):
        needed = total - val
        if needed in cache:
            return [cache[needed], pos]
        cache[val] = pos
    return []

print(find_pair([2, 7, 11, 15], 9))
