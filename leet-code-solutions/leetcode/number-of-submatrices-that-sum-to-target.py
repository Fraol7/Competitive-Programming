class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row, col = len(matrix), len(matrix[0])
        sub_sum = [[0]*col for _ in range(row)]
        ctr = 0
        for r in range(row):
            for c in range(col):
                top = sub_sum[r-1][c] if r > 0 else 0
                left = sub_sum[r][c-1] if c > 0 else 0
                top_left = sub_sum[r-1][c-1] if r>0 and c>0 else 0
                sub_sum[r][c] = matrix[r][c] + top + left - top_left
        
        for r1 in range(row):
            for r2 in range(r1, row):
                refer = defaultdict(int)
                refer[0] = 1
                for c in range(col):
                    curr = sub_sum[r2][c] - (sub_sum[r1-1][c] if r1>0 else 0)
                    ctr += refer[curr-target]
                    refer[curr] += 1
        return ctr
