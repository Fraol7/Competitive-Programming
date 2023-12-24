class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                k = 3*(i // 3) + j // 3
                if element != '.':
                    res += [('row', i, element), ('col', j, element), ('square', k, element)]
        return len(res) == len(set(res))
