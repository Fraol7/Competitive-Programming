class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        #three pointer i,j,k
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while k > j:
                trio = nums[i]+nums[j]+nums[k]
                if trio < 0:
                    j += 1
                elif trio > 0:
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while k > j and nums[j] == nums[j-1]:
                        j += 1    
        return ans
                