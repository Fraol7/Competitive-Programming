class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ctr = 0
        piles.sort()
        piles = piles[::-1]
        l = 1
        for i in range(len(piles)//3):
            ctr += piles[l]
            l += 2
        return ctr
