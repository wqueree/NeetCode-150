from collections import defaultdict
from typing import Dict, List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts: Dict[int, int] = defaultdict(int)
        frequencies: List[List[int]] = [[] for _ in range(len(nums) + 1)]

        nums.sort()
        for num in nums:
            counts[num] += 1
        for num, count in counts.items():
            frequencies[count].append(num)

        result: List[int] = []
        i: int = len(nums)
        while len(result) < k:
            result += frequencies[i]
            i -= 1
        return result
