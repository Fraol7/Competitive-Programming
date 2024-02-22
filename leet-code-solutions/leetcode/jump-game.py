class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if good - i <= nums[i]:
                good = i
        return True if good == 0 else False

        