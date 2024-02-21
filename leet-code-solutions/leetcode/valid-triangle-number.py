class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)           
        ptr, n = 0, len(nums)-2
        count = 0
        while ptr < n:
            left, right = ptr+1, n+1
            while left < right:
                if nums[ptr] < nums[left]+nums[right]:
                    count += right-left
                    left += 1
                else:
                    right -= 1
            ptr += 1
        return count

        