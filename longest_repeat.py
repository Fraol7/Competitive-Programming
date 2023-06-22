class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        freq = {}
        max_count = 0
        longest = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_count = max(max_count, freq[s[right]])
            if right - left + 1 - max_count > k:
                freq[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest
