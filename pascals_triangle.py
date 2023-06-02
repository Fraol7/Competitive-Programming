class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        lastRow = self.getRow(rowIndex-1)
        ans = [1]
        for i in range(len(lastRow)-1):
            ans.append(lastRow[i]+lastRow[i+1])
        ans.append(1)
        return ans
