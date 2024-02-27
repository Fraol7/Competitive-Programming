class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(score, nums, turn):
            if len(nums) == 1:
                return score + nums[0] if turn else score - nums[0]
            if turn:
                return max(helper(score + nums[0], nums[1:], False),
                           helper(score + nums[-1], nums[:len(nums)-1], False))
            else:
                return min(helper(score - nums[0], nums[1:], True),
                           helper(score - nums[-1], nums[:len(nums)-1], True))
        return helper(0, nums, True) >= 0
