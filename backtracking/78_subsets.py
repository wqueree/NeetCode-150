from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        self.search(sorted(nums), 0, [], result)
        return result
        
    def search(self, nums: List[int], index: int, path: List[int], result: List[List[int]]) -> None:
        result.append(path)
        for i in range(index, len(nums)):
            self.search(nums, i + 1, path + [nums[i]], result)
