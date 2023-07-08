class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        if num == 1:
            return True
        while left < right:
            mid = left + (right - left)//2
            val = mid**2
            if val == num:
                return True
            elif val < num:
                left = mid + 1
            else:
                right = mid
        return False
