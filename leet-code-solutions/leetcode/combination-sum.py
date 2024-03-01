class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        def backtrack(candidates,combined):
            if not candidates or sum(combined) > target:
                return
            if sum(combined) == target:
                self.answer.append(combined.copy())
                return
            for i in range(len(candidates)):
                backtrack(candidates[i:],combined+[candidates[i]])
        backtrack(candidates, [])
        return self.answer

