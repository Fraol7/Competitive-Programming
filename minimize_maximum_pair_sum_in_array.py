class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_val = 0
        num = len(nums)-1
        frntIndx = 0
        for bckIndx in range(num, num//2, -1):
            pairSum = nums[frntIndx] + nums[bckIndx]
            max_val = max(max_val, pairSum)
            frntIndx += 1
        return max_val
