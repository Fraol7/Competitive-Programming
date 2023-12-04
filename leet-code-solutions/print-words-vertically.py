class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        maxlen = 0
        j = 0
        for i in s:
            maxlen = max(maxlen, len(i))
        row = maxlen
        col = len(s)
        matrix = [[" "]*col for i in range(row)]
        for strr in s:
            n = len(strr)
            for i in range(n):
                matrix[i][j] = strr[i]
            j += 1
        finalstr = ["".join(substr).rstrip() for substr in matrix]
        return finalstr
        