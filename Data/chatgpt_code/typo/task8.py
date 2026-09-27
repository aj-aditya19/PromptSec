def top_k_frequent(nums, k):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    return [num for num, _ in sorted(counts.items(), key=lambda item: item[1], reverse=True)[:k]]
