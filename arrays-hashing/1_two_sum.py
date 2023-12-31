from typing import Dict, List, Union

class Solution:
    def twoSum(self, nums: List[int], target: int) -> Union[List[int], None]:
        complements: Dict[int, int] = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            complements[num] = i