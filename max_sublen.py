class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, right = 0, 0
        subcost = 0
        max_subLen = 0
        while right < len(s):
            subcost += abs(ord(s[right]) - ord(t[right]))
            if subcost > maxCost:
                subcost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            right += 1
            max_subLen = max(max_subLen, right - left)
        return max_subLen
