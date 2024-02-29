class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                for k in range(i, j+1):
                    if s[k].lower() not in s[i:j+1] or s[k].upper() not in s[i:j+1]:
                        break
                else: 
                    answer = max(answer, s[i:j+1], key=lambda x:len(x))   
        return answer 
