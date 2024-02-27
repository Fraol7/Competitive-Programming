class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s):
            temp = ""
            i, n = 0, len(s)
            while i < n:
                if s[i].isalpha():
                    temp += s[i]
                elif s[i].isdigit():
                    c = ''
                    while s[i].isdigit():
                        c += s[i]
                        i += 1
                    c = int(c) 
                    stack = 1
                    i += 1
                    j = i
                    while j < n and stack:
                        if s[j] == "[":
                            stack += 1
                        elif s[j] == "]":
                            stack -= 1
                        j += 1
                    temp += helper(s[i:j-1])*c
                    i = j-1
                i += 1
            return temp
        return helper(s)
