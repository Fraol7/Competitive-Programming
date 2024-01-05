class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            idx0, idx1 = max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])
            if idx0 <= idx1:
                result.append([idx0, idx1])
            if i+1 < len(firstList) and secondList[j][1] >= firstList[i+1][0]:
                i += 1
            elif j+1 < len(secondList) and firstList[i][1] >= secondList[j+1][0]:
                j += 1
            else:
                i += 1
                j += 1
        return result