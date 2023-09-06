class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island=0
        size_y=len(grid)
        size_x=len(grid[0])
        def find_one_island(i,j):
            if size_y > i and i >= 0 and size_x > j and j >= 0 and grid[i][j] == "1":
                grid[i][j] = "0"
                find_one_island(i,j-1)
                find_one_island(i,j+1)
                find_one_island(i-1,j)
                find_one_island(i+1,j)
            else:
                return

        for i in range(0,size_y):
            for j in range(0,size_x):
                if grid[i][j] == "1":
                    num_island += 1
                    find_one_island(i,j)
                    
        return num_island



