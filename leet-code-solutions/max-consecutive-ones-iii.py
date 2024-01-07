class Solution:
    def longestOnes(self, nums: List[int], K: int) -> int:
        left, right = 0, 0
        while right < len(nums):
            if nums[right] == 0:
                K -= 1
            if K < 0:
                if nums[left] == 0:
                    K += 1
                left += 1
            right += 1
        return right - left