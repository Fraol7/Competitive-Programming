class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        curr = [0]*k
        ans = 10**8

        if k == len(cookies):
            return max(cookies)
        def backtrack(idx, curr):
            nonlocal ans
            if idx == len(cookies):
                maxm = max(curr)
                ans = min(ans,maxm)
                return
            if ans <= max(curr):
                return
            for i in range(k):
                curr[i] += cookies[idx]
                backtrack(idx+1, curr)
                curr[i] -= cookies[idx]
        backtrack(0,curr)
        return ans
