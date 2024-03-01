class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1,10)]
        self.answer = []
        def subsets(arr):
            if not arr:
                if arr not in self.answer and len(arr) == k and sum(arr) == n:
                    self.answer.append(arr)
                return
            if arr not in self.answer and len(arr) == k and sum(arr) == n:
                self.answer.append(arr)
            for num in arr:
                new_arr = arr.copy()
                new_arr.remove(num)
                subsets(new_arr)
        subsets(nums)
        return self.answer