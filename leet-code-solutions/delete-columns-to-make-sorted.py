class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        arr = []
        for i in range(len(strs)-1):
            for j in range(len(strs[0])):
                if strs[i][j] > strs[i+1][j]:
                    arr.append(j)
        return len(set(arr))