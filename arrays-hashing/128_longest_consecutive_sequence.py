from typing import List, Set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set: Set[int] = set(nums)
        longest: int = 0
        for num in num_set:
            if (num - 1) not in num_set:
                current: int = 1
                while (num + current) in num_set:
                    current += 1
                longest = max(longest, current)
        return longest
