from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        prefixes: List[int] = [1] * n
        suffixes: List[int] = [1] * n
        answer: List[int] = [1] * n
        for i in range(1, n):
            prefixes[i] = prefixes[i - 1] * nums[i - 1]
            suffixes[n - i - 1] = suffixes[n - i] * nums[n - i]
        for i in range(n):
            answer[i] = prefixes[i] * suffixes[i]
        return answer
