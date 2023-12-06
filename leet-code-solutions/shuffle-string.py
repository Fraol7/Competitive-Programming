class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        astring = ['']*len(s)
        for i in range(len(s)):
            temp = indices[i]
            astring[temp] = s[i]
        return ''.join(astring)