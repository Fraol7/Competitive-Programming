class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        for i in range(min(len(v[0]),len(v[-1]))):
            if(v[0][i]!=v[-1][i]):
                return ans
            ans+=v[0][i]
        return ans 
                
