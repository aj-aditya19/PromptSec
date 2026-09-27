"""Variant: SYNONYM | Task 8"""

from typing import List
from collections import Counter

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    return [item for item, freq in count.most_common(k)]
