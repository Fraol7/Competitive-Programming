class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ctr, patches, curr, prefix = 1, 0, 0, 0
        while prefix < n:
            if curr < len(nums) and nums[curr] <= ctr:
                prefix += nums[curr]
                curr += 1
            else:
                prefix += ctr
                patches += 1
            ctr = prefix + 1
        return patches




