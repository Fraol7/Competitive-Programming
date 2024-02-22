class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix, result = nums[0], nums[0]
        for i in range(1, len(nums)):
            prefix += nums[i]
            result = max(((prefix+i) // (i+1)), result)
        return result 