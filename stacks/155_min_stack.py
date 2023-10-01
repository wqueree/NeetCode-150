from typing import List

class MinStack:

    def __init__(self):
        self.data: List[int] = [0] * 30000
        self.min_indices: List[int] = [0] * 30000
        self.top_index: int = -1
        self.min_index: int = -1

    def push(self, val: int) -> None:
        self.top_index += 1
        self.data[self.top_index] = val
        if self.min_index == -1 or val < self.data[self.min_indices[self.min_index]]:
            self.min_index += 1
            self.min_indices[self.min_index] = self.top_index

    def pop(self) -> None:
        self.top_index -= 1
        if self.top_index < self.min_indices[self.min_index]:
            self.min_index -= 1

    def top(self) -> int:
        return self.data[self.top_index]

    def getMin(self) -> int:
        return self.data[self.min_indices[self.min_index]]
