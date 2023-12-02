from typing import List


class Solution:


    def rob_range(self, nums_range: List[int]) -> int:
        dp: List[int] = [0 for _ in range(len(nums_range))]
        dp[0], dp[1] = nums_range[0], nums_range[1]
        for i in range(2, len(nums_range)):
            dp[i] = nums_range[i] + max(dp[: i - 1])
        return max(dp)


    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        return max(self.rob_range(nums[:-1]), self.rob_range(nums[1:]))
