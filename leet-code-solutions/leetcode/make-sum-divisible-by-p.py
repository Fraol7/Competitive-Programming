class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        curr = sum(nums)
        if curr < p:
            return -1
        if 0 == curr % p:
            return 0
        prefix = 0
        refer = {0: 0}
        mini = len(nums)
        for index, val in enumerate(nums):
            prefix += val
            remainder = (prefix - curr) % p
            if remainder in refer:
                mini = min(mini, (index + 1 - refer[remainder]))
            refer[prefix % p] = index + 1 
        return mini if mini < len(nums) else -1
        