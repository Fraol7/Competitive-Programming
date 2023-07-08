
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = left + (right - left)//2
            val = mid**2
            if val == x:
                return mid
            if val > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
    
