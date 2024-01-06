class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lt, rt, ctr = 0, len(nums)-1, 0
        while ctr <= rt:
            if nums[ctr] == 2:
                nums[ctr], nums[rt] = nums[rt], nums[ctr]
                rt -= 1
            elif nums[ctr] == 0:
                nums[ctr], nums[lt] = nums[lt], nums[ctr]
                lt += 1
                ctr += 1
            else:
                ctr += 1