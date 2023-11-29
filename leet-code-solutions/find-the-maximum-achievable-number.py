class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        num += 2*t
        return num