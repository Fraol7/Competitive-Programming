class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans, k = [], len(p)
        target = Counter(p)
        window = Counter(s[:k])
        if target == window:
            ans.append(0)
        for i in range(len(s)-k):
            window[s[i]] -= 1
            window[s[i+k]] = window.get(s[i+k], 0) + 1
            if window[s[i]] == 0:
                del window[s[i]]
            if target == window:
                ans.append(i+1)
        return ans
