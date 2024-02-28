class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutes = []
        def helper(arr, temp):
            if len(arr) == 1:
                self.permutes.append(temp+[arr[0]])
                return
            for num in arr:
                if num not in temp:
                    new_arr = arr.copy()
                    new_arr.remove(num)
                    helper(new_arr, temp+[num])
        helper(nums, [])
        return self.permutes