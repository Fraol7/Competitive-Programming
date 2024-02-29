class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def helper(arr,idx):
            if idx < len(nums):
                for i in range(idx,len(nums)):
                    helper(arr+[nums[i]],i+1)
            self.ans.append(arr)
        helper([],0)
        return self.ans
        