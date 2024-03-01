class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        candidates.sort()
        def backtrack(candidates,combined):
            if sum(combined) == target and combined.copy() not in self.answer:
                self.answer.append(combined.copy())
                return
            if not candidates or sum(combined) > target:
                return
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                backtrack(candidates[i+1:],combined+[candidates[i]])
        backtrack(candidates, [])
        return self.answer



