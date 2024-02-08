class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix = [0]
        ctr = 0
        for i in range(len(s)):
            prefix.append(prefix[-1]+int(s[i]))
        for j in range(len(s)):
            if s[j] == '0':
                ctr += prefix[j]*(prefix[-1]-prefix[j])
            else:
                ctr += (j-prefix[j])*(len(s)-1-j-prefix[-1]+prefix[j+1])
        return ctr