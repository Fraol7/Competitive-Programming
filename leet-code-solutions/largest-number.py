class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        while True:
            flag = 0
            for j in range(len(nums)-1):
                if nums[j]+nums[j+1] < nums[j+1]+nums[j]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]
                    flag += 1
            if flag == 0:
                break
        return str(int("".join(nums)))