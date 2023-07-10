class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        leftProd = 1
        rightProd = 1
        for i in range(len(nums)):
            ans[i] *= leftProd
            leftProd = leftProd*nums[i]
            ans[(len(nums)-1)-i] *= rightProd
            rightProd = rightProd*nums[(len(nums)-1)-i]
        return(ans)
