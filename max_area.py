class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def traverse(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            area = 1
            grid[row][col] = 0
            area += traverse(row, col + 1)
            area += traverse(row, col - 1)
            area += traverse(row + 1, col)
            area += traverse(row - 1, col)
            return area
        
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, traverse(i, j))
        return maxArea
