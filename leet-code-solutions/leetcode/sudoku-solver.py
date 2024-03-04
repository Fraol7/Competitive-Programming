class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.row = [set() for _ in range(9)]
        self.col = [set() for _ in range(9)]
        self.sqr = [set() for _ in range(9)]
        self.nodot = False
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    k = 3*(i//3)+j//3
                    num = int(board[i][j])
                    self.row[i].add(num)
                    self.col[j].add(num)
                    self.sqr[k].add(num)
        def backtrack(i,j):
            if i == 9:
                self.nodot = True
                return 
            if board[i][j].isdigit():
                backtrack(i+(j+1)//9, (j+1)%9)
            else:
                for num in range(1, 10):
                    k = 3*(i//3)+j//3
                    if num not in self.row[i] and num not in self.col[j] and num not in self.sqr[k]:
                        board[i][j] = str(num)
                        self.row[i].add(num)
                        self.col[j].add(num)
                        self.sqr[k].add(num)

                        backtrack(i+(j+1)//9, (j+1)%9)

                        if not self.nodot:
                            board[i][j] = "."
                            self.row[i].remove(num)
                            self.col[j].remove(num)
                            self.sqr[k].remove(num)
        backtrack(0,0)







        