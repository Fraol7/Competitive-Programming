class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:x[1])
        arrows = len(points)
        check = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= check:
                check = min(check, points[i][1])
                arrows -= 1
            else:
                check = points[i][1]
        return arrows
    