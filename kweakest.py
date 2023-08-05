class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lis = []
        heapify(lis)
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if(mat[i][j] == 0):
                    break
                else:
                    count += 1
            heappush(lis, [count, i])
        final = []
        while(k):
            a = heappop(lis)
            final.append(a[1])
            k -= 1
        return(final)
