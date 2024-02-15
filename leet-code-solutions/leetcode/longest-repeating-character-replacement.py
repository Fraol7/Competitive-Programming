class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        refer = defaultdict(int)
        left, freq, longest = 0, 0, 0
        for right in range(len(s)):
            refer[s[right]] += 1
            freq = max(freq, refer[s[right]])
            if right-left+1 - freq > k:
                refer[s[left]] -= 1
                left += 1
            longest = max(longest, right-left+1)
        return longest
