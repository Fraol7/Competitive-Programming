class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        i = 0
        j = len(mat) - 1
        while j > -1:
            if i != j:
                result += mat[i][i]
                result += mat[i][j]
            else:
                result += mat[i][j]
            i += 1
            j -= 1
        return result