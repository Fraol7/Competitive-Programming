class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: 
            return False
        min_val = nums[0]
        if nums[1] > min_val:
            i = 2
            point = nums[1]
        else:
            point = inf
            i = 1
        for j in range(i,len(nums)):
            if nums[j] > point:
                return True
            if nums[j] < min_val:
                min_val = nums[j]
            elif nums[j] < point and nums[j] > min_val:
                point = nums[j]
        return False