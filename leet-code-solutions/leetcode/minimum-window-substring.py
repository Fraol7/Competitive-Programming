class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        refer = defaultdict(int)
        for char in t:
            refer[char] += 1
        ctr = len(t)
        window = [0, len(s)+1]
        start = 0
        for end, char in enumerate(s):
            if refer[char] > 0:
                ctr -= 1
            refer[char] -= 1
            if ctr == 0:
                while True:
                    if refer[s[start]] == 0:
                        break
                    refer[s[start]] += 1
                    start += 1
                if end - start < window[1] - window[0]:
                    window = [start, end]
                refer[s[start]] += 1
                ctr += 1
                start += 1
        return '' if window[1] > len(s) else s[window[0]:window[1]+1]