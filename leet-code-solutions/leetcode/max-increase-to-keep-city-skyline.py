class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp = min(max(grid[i]), max([grid[i][j] for i in range(len(grid))]))
                total += temp-grid[i][j]
        return total