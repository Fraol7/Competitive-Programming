class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ctr = 0
        for i in s:
            if i == "(":
                stack.append(i)
                ctr += 1
            elif stack:
                stack.pop()
                ctr -= 1
            else:
                ctr += 1
        return ctr