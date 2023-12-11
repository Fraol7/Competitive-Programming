class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        left, right = 0, 1
        for i in nums:
            if i > 0:
                ans[left] = i
                left += 2
            else:
                ans[right] = i
                right += 2
        return ans