def find_pair_sum(array, target):
    """Searches and identifies element pairs"""
    mapping = {}
    for i, elem in enumerate(array):
        need = target - elem
        if need in mapping:
            return [mapping[need], i]
        mapping[elem] = i
    return []
