from collections import defaultdict
from typing import Dict, List, Set


class Solution:


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees: Dict[int, int] = defaultdict(int)
        adjacents: Dict[int, Set[int]] = defaultdict(set)
        
        for curr, prev in prerequisites:
            indegrees[curr] += 1
            adjacents[prev].add(curr)
            
        no_deps: List[int] = [i for i in range(numCourses) if not i in indegrees]
        order: List[int] = []
        while no_deps:
            curr: int = no_deps.pop()
            order.append(curr)
            for adjacent in adjacents[curr]:
                indegrees[adjacent] -= 1
                if indegrees[adjacent] == 0:
                    no_deps.append(adjacent)
                    
        return len(order) == numCourses
