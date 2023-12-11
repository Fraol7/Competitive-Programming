from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = Counter(arr)
        mod = int(len(arr) * 0.25)
        for i in freq:
            if freq[i] > mod:
                return i