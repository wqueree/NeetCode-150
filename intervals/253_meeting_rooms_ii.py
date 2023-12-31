import heapq
from typing import List


class Solution:


    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda times: times[0])
        rooms: List[int] = [intervals[0][1]]
        for i in range(1, len(intervals)):
            meeting_start, meeting_end = intervals[i]
            if rooms[0] <= meeting_start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, meeting_end)
        return len(rooms)
