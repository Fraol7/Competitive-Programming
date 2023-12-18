class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        Dict = {}
        for i,num in enumerate(nums):
            Dict[num] = i
        for k,j in operations:
            nums[Dict[k]] = j
            Dict[j] = Dict[k]
        return nums