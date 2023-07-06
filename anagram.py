from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        p_freq = Counter(p)
        window_freq = Counter(s[:len(p)])
        left = 0
        right = len(p) - 1
        ans = []
        
        while right < len(s):
            if p_freq == window_freq:
                ans.append(left)
                
            window_freq[s[left]] -= 1
            if window_freq[s[left]] == 0:
                del window_freq[s[left]]
            
            left += 1
            right += 1
            if right < len(s):
                window_freq[s[right]] += 1
        
        return ans
