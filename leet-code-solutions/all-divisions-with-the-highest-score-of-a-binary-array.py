class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        prefixsum = [nums[0]]
        check = []
        result = []
        
        for i in range(1,len(nums)):
            prefixsum.append(prefixsum[-1] + nums[i])

       
        for i in range(len(prefixsum)+1):
            zeros = i-prefixsum[i-1] if i != 0 else 0
            ones = prefixsum[-1] - prefixsum[i-1] if i!=0 else prefixsum[-1]
            check.append(zeros + ones) 
        max_val = max(check)
        
        for i,num in enumerate(check):
            if num == max_val:
                result.append(i)
                
        return result 
        