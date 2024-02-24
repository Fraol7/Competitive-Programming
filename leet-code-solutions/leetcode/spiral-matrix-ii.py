class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        m, k = 0, n
        row, col = 0, 0
        val = 1
        while m < (n+1)//2:
            for i in range(col, k):
                matrix[row][i] = val
                val += 1
            for j in range(row+1,k):
                matrix[j][k-1] = val
                val += 1
            for i in range(k-2,col-1,-1):
                matrix[k-1][i] = val
                val += 1
            for j in range(k-2,row, -1):
                matrix[j][col] = val
                val += 1
            m += 1
            k -= 1
            row += 1
            col += 1
        return matrix
