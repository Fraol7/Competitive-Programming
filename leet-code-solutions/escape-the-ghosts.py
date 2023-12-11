class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        pd = abs(target[0]) + abs(target[1])
        for g in ghosts:
            gd = abs(g[0] - target[0]) + abs(g[1] - target[1])
            if gd <= pd:
                return False
        return True
