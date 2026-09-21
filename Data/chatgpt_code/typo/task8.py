# Prompt:
# Write a Python fucntion that, given an integr aray nums and an integer k, returns the k most frequnt elemnts.

from collections import Counter

def top_k_frequent(nums, k):
    return [num for num, _ in Counter(nums).most_common(k)]
