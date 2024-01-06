class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wind = sum(nums[:k])
        maxi = wind/k
        for i in range(len(nums)-k):
            wind -= nums[i]
            wind += nums[i+k]
            maxi = max(maxi, wind/k)
        return maxi