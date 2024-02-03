class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j, curr, ctr = 0, 0, float('inf')
        for i in range(len(nums)):
            curr += nums[i]
            while curr >= target:
                ctr = min(ctr, i-j+1)
                curr -= nums[j]
                j += 1
        if ctr == float('inf'):
            return 0
        return ctr