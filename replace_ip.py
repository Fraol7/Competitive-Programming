class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        if len(s) > 12:
            return ans
        def backtrack(idx, dots, currIP):
            if dots == 4 and idx == len(s):
                ans.append(currIP[:-1])
            for i in range(idx, min(len(s), idx+3)):
                if int(s[idx:i+1]) < 256 and (i == idx or s[idx] != "0"):
                    backtrack(i+1, dots + 1, currIP + s[idx:i+1] + '.')
        backtrack(0, 0, "")
        return ans
