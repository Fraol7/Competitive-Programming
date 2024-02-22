class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        refer, score = [], 0
        for i in range(1, len(weights)):
            refer.append(weights[i]+weights[i-1])
        refer.sort(reverse=True)
        for i in range(k-1):
            score += refer[i] - refer[-1-i]
        return score