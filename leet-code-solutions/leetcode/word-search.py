class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row, self.col = len(board), len(board[0])
        def isValid(row, col, visited):
            return (row >= 0 and row < self.row) and (col >= 0 and col < self.col) and (row,col) not in visited
        
        def backtrack(i,j,combined,visited,ctr):
            if combined == word:
                return True
            if len(combined) > len(word):
                return False
            for r,c in [(1,0), (0,1), (-1,0), (0,-1)]:
                if isValid(i+r, j+c, visited) and board[i+r][j+c] == word[ctr]:
                    if backtrack(i+r, j+c, combined+board[i+r][j+c], visited|set([(i+r, j+c)]), ctr+1):
                        return True
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i, j, board[i][j],set([(i,j)]),1):
                        return True
        else:
            return False

        
            