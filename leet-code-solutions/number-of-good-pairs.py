class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ctr = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    ctr += 1
        return ctr