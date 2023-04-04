class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        answer = []
        _len = len(nums)
        nums = self.Sorted(nums, _len)
        for i in range(len(nums)):
            if nums[i] == target:
                answer.append(i)
        return answer

    def Sorted(self, array, size):
        for step in range(size):
            min_idx = step
            for i in range(step + 1, size):
                if array[i] < array[min_idx]:
                    min_idx = i
            (array[step], array[min_idx]) = (array[min_idx], array[step])
        return array
