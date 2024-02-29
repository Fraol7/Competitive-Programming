class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        def backtrack(combine, i):
            if sum(combine) > target or len(candidates) <= i:
                return
            if sum(combine) == target:
                self.result.append(combine.copy()) 
                return
            backtrack(combine+[candidates[i]], i)
            backtrack(combine, i+1)
        backtrack([], 0)
        return self.result

