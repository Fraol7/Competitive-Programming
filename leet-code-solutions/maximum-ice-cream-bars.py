class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ctr = 0
        for i in costs:
            if i > coins:
                return ctr
            coins -= i
            ctr += 1
        return ctr