class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0]-x[1])
        mini_cost = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                mini_cost += costs[i][0]
            else:
                mini_cost += costs[i][1]
        return mini_cost
        