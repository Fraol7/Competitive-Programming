class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ctr = 0
        for arr in grid:
            arr.sort()
            ctr += bisect_right(arr, -1)
        return ctr
