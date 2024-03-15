class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            temp = 0
            for num in piles:
                temp += (num-1)//k + 1
            if temp > h:
                return False
            return True

        left, right = 1, max(piles)
        if len(piles) == h:
            return max(piles)

        while left < right:
            mid = left + (right-left)//2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left
