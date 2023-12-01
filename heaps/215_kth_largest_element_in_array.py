import heapq
from typing import List


class Solution:
    
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: List[int] = list()
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
