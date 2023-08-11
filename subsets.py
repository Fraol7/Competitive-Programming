class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.length = len(nums)
        self.nums = nums
        self.backtrack([],0)
        return self.ans

    def backtrack(self,arr,ind):
        if ind < self.length:
            for i in range(ind,self.length):
                self.backtrack(arr+[self.nums[i]],i+1)
        self.ans.append(arr)
