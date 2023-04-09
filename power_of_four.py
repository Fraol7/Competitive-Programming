class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        else:
            while n > 3:
                n = n/4
            if n != 1:
                return False
            else: return True
