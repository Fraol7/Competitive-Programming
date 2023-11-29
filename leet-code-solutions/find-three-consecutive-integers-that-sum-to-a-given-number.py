class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3 != 0: return []
        temp = num//3
        return [temp - 1, temp, temp + 1]

        