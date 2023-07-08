class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = 0
        nums.sort()
        for i in nums:
            if i != l:
                return l
            l += 1
        return l
