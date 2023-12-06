class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        answer = []
        for i in set(nums):
            if nums.count(i) > len(nums) // 3:
                answer.append(i)
        return answer
