class Solution:
    def countUnguarded(self, m, n, guards, walls):
        grid = [[0] * n for _ in range(m)]
        for coord in guards:
            grid[coord[0]][coord[1]] = 'g'
        for coord in walls:
            grid[coord[0]][coord[1]] = 'w'

        for coord in guards:
            row, col = coord
            for i in range(row + 1, m):
                if grid[i][col] == 'g' or grid[i][col] == 'w':
                    break
                grid[i][col] = 1
            for i in range(row - 1, -1, -1):
                if grid[i][col] == 'g' or grid[i][col] == 'w':
                    break
                grid[i][col] = 1

            for j in range(col + 1, n):
                if grid[row][j] == 'g' or grid[row][j] == 'w':
                    break
                grid[row][j] = 1
            for j in range(col - 1, -1, -1):
                if grid[row][j] == 'g' or grid[row][j] == 'w':
                    break
                grid[row][j] = 1
        free_space = 0
        for row in grid:
            free_space += row.count(0)
        return free_space
