from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merge: List[List[int]] = list()
        for interval in intervals:
            if not merge or interval[0] > merge[-1][1]:
                merge.append(interval)
            else:
                if interval[1] > merge[-1][1]:
                    merge[-1][1] = interval[1]
        return merge
