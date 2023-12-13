class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        answer = [pivot]
        nums.remove(pivot)
        ctr = 0
        for anum in nums:
            if anum < pivot:
                answer.insert(ctr, anum)
                ctr += 1
            elif anum > pivot:
                answer.insert(len(answer), anum)
            else:
                answer.insert(answer.index(pivot), anum)
        return answer