class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            result.append(row)
        return result