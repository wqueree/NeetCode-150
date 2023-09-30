from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        n: int = len(nums)
        if n == 1:
            return nums[0]
        dp: List[int] = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = nums[i] + max(dp[: i - 1])
        return max(dp)
