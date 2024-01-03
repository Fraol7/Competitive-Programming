class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ctr = 0
        nums.sort()
        for slow in range(len(nums)-1):
            fast = slow + 1
            while fast < len(nums) and nums[slow] + nums[fast] < target:
                ctr += 1
                fast += 1
        return ctr