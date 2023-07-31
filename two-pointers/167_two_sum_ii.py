from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left: int = 0
        right: int = len(numbers) - 1
        while left < right:
            test_sum: int = numbers[left] + numbers[right]
            if test_sum == target:
                return [left + 1, right + 1]
            if test_sum < target:
                left += 1
            else:
                right -= 1
