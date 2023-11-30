class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        res = 0
        for i in range(1, len(salary)-1):
            res += salary[i]
        return res/(len(salary)-2)
        