class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return s
                elif s > target:
                    right -= 1
                else:
                    left += 1
                if abs(s - target) < abs(ans - target):
                    ans = s
        return ans