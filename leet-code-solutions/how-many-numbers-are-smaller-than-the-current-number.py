class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ctr = 0
            for j in nums:
                if j < i:
                    ctr += 1
            ans.append(ctr)
        return ans
                