class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        Oddans = []
        Evenans = []
        for i in nums:
            if i%2 == 0:  Evenans.append(i)
            else:  Oddans.append(i)
        return Evenans + Oddans
            
