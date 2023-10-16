class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) < 2:
            return 0
        maxi = 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            maxi = max(maxi, diff)
        return maxi
