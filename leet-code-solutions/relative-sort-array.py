class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3, result = [], []
        set2 = set(arr2)
        for i in arr1:
            if i not in set2:
                arr3.append(i)
        arr3.sort()
        for j in arr2:
            ctr = arr1.count(j)
            result.extend([j]*ctr)
        result.extend(arr3)
        return result

