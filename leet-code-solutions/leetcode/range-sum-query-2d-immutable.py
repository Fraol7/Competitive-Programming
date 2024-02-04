class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.sums = [[]]
        else:
            rows, cols = len(matrix), len(matrix[0])
            self.sums = [[0] * (cols + 1) for _ in range(rows + 1)]
            for i in range(rows - 1, -1, -1):
                for j in range(cols - 1, -1, -1):
                    self.sums[i][j] = matrix[i][j] + self.sums[i + 1][j] + self.sums[i][j + 1] - self.sums[i + 1][j + 1]
        print(self.sums)
    def sumRegion(self, row1, col1, row2, col2):
        return self.sums[row1][col1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1] + self.sums[row2 + 1][col2 + 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)