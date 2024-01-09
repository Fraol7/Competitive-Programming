class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxi = 0
        curr = s[:k].count('a') + s[:k].count('e') + s[:k].count('i') + s[:k].count('o') + s[:k].count('u')
        ctr = curr
        for i in range(k,len(s)):
            if s[i] in {'a','e','i','o','u'}:
                curr += 1
            if s[i-k] in {'a','e','i','o','u'}:
                curr -= 1
            ctr = max(ctr,curr)
        return ctr