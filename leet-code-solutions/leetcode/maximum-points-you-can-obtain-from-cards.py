class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_score = sum(cardPoints)
        k = len(cardPoints)-k
        total_score = sum(cardPoints[:k])
        min_score = float('inf')
        for i in range(len(cardPoints)-k):
            min_score = min(min_score, total_score)
            total_score -= cardPoints[i]
            total_score += cardPoints[i+k]
        min_score = min(min_score, total_score)
        return max_score - min_score
