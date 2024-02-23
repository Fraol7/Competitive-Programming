class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        i = len(nums)-1
        ans = 0 
        while i > 0:
            if nums[i] < nums[i-1]:
                space = ceil(nums[i-1]/nums[i])
                left = nums[i-1]//space
                nums[i-1] = left
                ans += space - 1
            i -= 1
        return ans
