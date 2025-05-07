from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)
        most_frequent_numbers = heapq.nlargest(k, frequency_map.keys(), key=frequency_map.get)

        return most_frequent_numbers
