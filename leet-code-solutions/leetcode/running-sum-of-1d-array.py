class Solution(object):
    def runningSum(self, nums):
        if len(nums) == 1:
            return nums
        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(result[-1] + nums[i])
        return result