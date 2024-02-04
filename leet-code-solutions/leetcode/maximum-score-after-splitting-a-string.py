class Solution:
    def maxScore(self, s: str) -> int:
        prefix = [int(s[0])]
        for i in range(1, len(s)-1):
            prefix.append(prefix[-1] + int(s[i]))
        total = prefix[-1] + int(s[-1])
        max_val = 0
        for j in range(1, len(s)):
            max_val = max(max_val, j + total - 2*prefix[j-1])
        return max_val