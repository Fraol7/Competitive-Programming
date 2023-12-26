class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_val = flips[0]
        ctr = 0
        for idx, val in enumerate(flips):
            max_val = max(max_val, val)
            if idx+1 == max_val:
                ctr += 1
        return ctr