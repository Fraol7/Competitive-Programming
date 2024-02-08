class Solution:
    def balancedString(self, s: str) -> int:
        refer = Counter(s)
        each = len(s)//4
        max_diff = 0
        for i in 'QWER':
            if refer[i] - each > 0:
                max_diff += refer[i] - each
                refer[i] -= each
            else:
                del refer[i]
        if max_diff == 0 or max_diff == 1:
            return max_diff
        left, min_win = 0, float('inf')
        for right in range(len(s)):
            if s[right] in refer:
                refer[s[right]] -= 1
                if refer[s[right]] >= 0:
                    max_diff -= 1
            while left < right and max_diff == 0:
                min_win = min(min_win, right-left+1)
                if s[left] in refer:
                    refer[s[left]] += 1
                    if refer[s[left]] > 0:
                        max_diff += 1
                left += 1
        return min_win
