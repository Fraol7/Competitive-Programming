class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ctr, left, nice, curr = 0, 0, 0, 0
        for right in range(len(nums)):
            if nums[right]%2 == 1:
                curr += 1
                ctr = 0
            if curr == k:
                while left < len(nums) and nums[left] % 2 == 0:
                    ctr+=1
                    left += 1
                ctr += 1
                curr -= 1
                left += 1
            nice += ctr
        return nice