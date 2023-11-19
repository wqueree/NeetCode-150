from typing import List, Set, Tuple

class Solution:

    def getNeighbours(self, i: int, j: int, grid: List[List[str]]):
        neighbours: List[Tuple[int, int]] = list()
        if j > 0:
            neighbours.append((i, j - 1))
        if j < len(grid[0]) - 1:
            neighbours.append((i, j + 1))
        if i > 0:
            neighbours.append((i - 1, j))
        if i < len(grid) - 1:
            neighbours.append((i + 1, j))
        return neighbours

    def bfs(self, i: int, j: int, grid: List[List[str]], visited: Set[Tuple[int, int]]):
        queue: List[Tuple[int, int]] = [(i, j)]
        while queue:
            i, j = queue.pop(0)
            if (i, j) not in visited and grid[i][j] == "1":
                queue += self.getNeighbours(i, j, grid)
                visited.add((i, j))

    def numIslands(self, grid: List[List[str]]) -> int:
        visited: Set[Tuple[int, int]] = set()
        num_islands: int = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    num_islands += 1
                    self.bfs(i, j, grid, visited)
        return num_islands
