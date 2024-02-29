class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def helper(arr,idx):
            if idx < len(nums):
                for i in range(idx,len(nums)):
                    helper(arr+[nums[i]],i+1)
            arr.sort()
            if arr not in self.ans:
                self.ans.append(arr)
        helper([],0)
        return self.ans