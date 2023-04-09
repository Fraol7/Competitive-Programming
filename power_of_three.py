class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        else:
            while n > 2:
                n = n/3
            if n != 1:
                return False
            else: return True
