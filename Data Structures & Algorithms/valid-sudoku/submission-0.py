from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        GRID = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                ele = board[r][c]

                if (
                    ele in ROWS[r]
                    or ele in COLS[c]
                    or ele in GRID[(r // 3, c // 3)]
                ):
                    return False

                ROWS[r].add(ele)
                COLS[c].add(ele)
                GRID[(r // 3, c // 3)].add(ele)

        return True