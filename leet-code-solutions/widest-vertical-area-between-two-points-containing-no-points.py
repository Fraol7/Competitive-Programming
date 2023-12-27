class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        largest = 0
        for i in range(len(points)-1):
            largest = max(largest, points[i+1][0]-points[i][0])
        return largest