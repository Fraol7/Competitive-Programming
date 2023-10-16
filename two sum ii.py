class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left = i 
            right = len(numbers) - 1

            while left < right:
                twoSums = numbers[left] + numbers[right]
                if twoSums < target:
                    left +=1
                elif twoSums > target:
                    right-=1
                else:
                    return [left+1, right+1]


