class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene,0)])
        check = set(bank)
        while queue:
            curr,ctr = queue.popleft()
            if curr == endGene:
                return ctr
            for i in range(8):
                for char in "ACGT":
                    new = curr[:i] + char + curr[i+1:]
                    if new in check:
                        check.remove(new)
                        queue.append((new, ctr + 1))
        return -1
