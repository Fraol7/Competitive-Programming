class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left, right = 0, sum(nums)
        ans = [0] * len(nums)
        for i, num in enumerate(nums):
            ans[i] = right - left + (2*i - len(nums)) * num
            left += num
            right -= num
        return ans

