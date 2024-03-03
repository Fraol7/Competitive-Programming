class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."]*n for i in range(n)]

        def backtrack(row,cols,posDiags,negDiags):
            if row == n:
                result.append(["".join(line) for line in board])
                return
            for col in range(n):
                if col not in cols and row+col not in posDiags and row-col not in negDiags:
                    board[row][col] = "Q"
                    backtrack(row+1, cols|set([col]), posDiags|set([row+col]), negDiags|set([row-col]))
                    board[row][col] = "."
        backtrack(0,set(),set(),set())
        return result

