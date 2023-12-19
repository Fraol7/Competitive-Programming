class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        totalEvenSum = 0 
        result = []

        for num in nums:
            if num%2 == 0:
                totalEvenSum += num
                
        for val, idx in queries:
            oldVal = nums[idx]
            nums[idx] += val            
            if oldVal % 2 == 0:
                totalEvenSum -= oldVal
            if nums[idx] % 2 == 0:
                totalEvenSum += nums[idx]
            result.append(totalEvenSum)            
        return result
            