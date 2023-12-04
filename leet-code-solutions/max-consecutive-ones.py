class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        val = 0
        ctr = 0
        for i in nums:
            if ctr == ctr + i:
                val = max(val, ctr)
                ctr = 0
            else:
                ctr += i
        val = max(val, ctr)
        return val
        