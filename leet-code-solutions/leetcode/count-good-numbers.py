class Solution:
    def countGoodNumbers(self, n: int) -> int:
        x = n//2
        pow_x = pow(4, x, 10**9 + 7)
        y = n - x
        pow_y = pow(5, y, 10**9 + 7)
        return (pow_x*pow_y) % (10**9 + 7)