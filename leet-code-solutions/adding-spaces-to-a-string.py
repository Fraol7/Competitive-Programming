class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        idx = 0
        for i in spaces:
            result += s[idx:i]
            result += " "
            idx = i
        result += s[idx:]
        return(result)