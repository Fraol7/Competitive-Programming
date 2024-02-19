class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums += nums
        ans = [-1]*n
        stack = []
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                ans[idx] = nums[i]
            stack.append(i%n)
        return ans
