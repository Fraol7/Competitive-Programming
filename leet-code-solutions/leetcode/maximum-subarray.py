class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix=0
        maxi, mini = nums[0], 0
        for i in nums:
            prefix+=i
            maxi = max(maxi, prefix-mini)
            if prefix < mini:
                mini = prefix
        return maxi