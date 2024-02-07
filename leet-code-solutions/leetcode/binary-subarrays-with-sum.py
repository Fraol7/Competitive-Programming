class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix, ctr = 0,0
        refer = defaultdict(int)
        refer[0] = 1
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - goal in refer:
                ctr += refer[prefix - goal]
            refer[prefix] += 1
        return ctr
