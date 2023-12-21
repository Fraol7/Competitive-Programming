class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i, j, diag = 0, 0, 0
        n, m = len(mat[0]), len(mat)
        result = []
        while diag < m+n-1:
            if diag%2 == 0:
                while i>0 and j+1<n:
                    result.append(mat[i][j])
                    i -= 1
                    j += 1
                result.append(mat[i][j])
                if j+1==n:
                    i += 1
                else:
                    j += 1
            else:
                while j>0 and i+1<m:
                    result.append(mat[i][j])
                    j -= 1
                    i += 1
                result.append(mat[i][j])
                if i+1==m:
                    j += 1
                else:
                    i += 1
            diag += 1
        return result