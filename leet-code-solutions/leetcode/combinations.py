class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(candidate):
            if len(candidate) == k:
                result.append(candidate.copy())
                return
            last = candidate[-1] if candidate else 0
            for num in range(last+1, n+1):
                candidate.append(num)
                backtrack(candidate)
                candidate.pop()
        backtrack([])
        return result