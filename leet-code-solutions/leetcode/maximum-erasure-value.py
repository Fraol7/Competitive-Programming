class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        check = {nums[0]: 0}
        maxsum = nums[0]
        left = -1
        for right in range(1, len(nums)):
            if nums[right] in check:
                left = max(left, check[nums[right]])
            check[nums[right]] = right
            nums[right] += nums[right-1]
            if left != -1:
                arrsum = nums[right] - nums[left]
            else:
                arrsum = nums[right]
            maxsum = max(maxsum,  arrsum)
        return maxsum
        
        