class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        p1 = 0
        p2 = len(costs)-1

        while(p1 < candidates):
            heappush(heap, (costs[p1], p1))
            p1 += 1

        while(p2 >= len(costs)-candidates and p2 >= p1):
            heappush(heap, (costs[p2], p2))
            p2 -= 1

        res = 0
        for i in range(k):
            c, idx = heappop(heap)
            res += c

            if idx < p1:
                if p1 <= p2:
                    heappush(heap, (costs[p1], p1))
                    p1 += 1
            else:
                if p1 <= p2:
                    heappush(heap, (costs[p2], p2))
                    p2 -= 1
        return res


        
