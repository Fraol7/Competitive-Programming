class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        totset = set(fronts + backs)
        for f,b in zip(fronts, backs):
            if f == b:
                totset.discard(f) 
        return min(totset, default = 0)