from collections import Counter

def most_common_values(numbers, k):
    frequency = Counter(numbers)
    sorted_items = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]
