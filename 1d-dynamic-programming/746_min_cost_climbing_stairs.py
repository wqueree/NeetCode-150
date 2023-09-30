from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n: int = len(cost)
        dp: List[int] = [0 for _ in range(n + 1)]
        if n == 2:
            return min(cost[0], cost[1])
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
