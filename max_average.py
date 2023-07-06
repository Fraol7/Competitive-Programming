class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k - 1
        current_sum = sum(nums[left:right+1])
        max_average = current_sum / k
        
        while right < len(nums) - 1:
            right += 1
            current_sum += nums[right]
            current_sum -= nums[left]
            average = current_sum / k
            max_average = max(max_average, average)
            left += 1
        
        return max_average

