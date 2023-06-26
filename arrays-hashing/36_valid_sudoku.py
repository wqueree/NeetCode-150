from collections import defaultdict
from typing import Dict, List, Set, Tuple

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        EMPTY: str = "."
        row_checks: Dict[int, Set] = defaultdict(set)
        col_checks: Dict[int, Set] = defaultdict(set)
        box_checks: Dict[Tuple[int, int], Set] = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == EMPTY:
                    continue
                if board[i][j] in row_checks[i]:
                    return False
                else:
                    row_checks[i].add(board[i][j])
                if board[i][j] in col_checks[j]:
                    return False
                else:
                    col_checks[j].add(board[i][j])
                if board[i][j] in box_checks[(i // 3, j // 3)]:
                    return False
                else:
                    box_checks[(i // 3, j // 3)].add(board[i][j])
        return True
