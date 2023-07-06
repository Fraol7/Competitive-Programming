class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)
