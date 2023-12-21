class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid)-2, len(grid[0])-2
        largest = 0
        for i in range(n):
            for j in range(m):
                value = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                largest = max(largest, value)
        return largest