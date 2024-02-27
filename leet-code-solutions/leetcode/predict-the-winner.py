class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(nums, left, right):
            if left > right:
                return 0
            if left == right:
                return nums[left]
            score = max(nums[left] + min(helper(nums, left + 2, right),helper(nums, left + 1, right - 1)),nums[right] + min(helper(nums, left, right - 2),helper(nums, left + 1, right - 1)))
            return score
        return helper(nums, 0, len(nums) - 1) >= sum(nums)/2
