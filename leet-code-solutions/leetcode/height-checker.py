class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected, ctr = sorted(heights), 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                ctr += 1
        return ctr