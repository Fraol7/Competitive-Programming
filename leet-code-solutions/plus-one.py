class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num, ctr = 0, 1
        for i in range(len(digits)-1, -1, -1):
            num += ctr * digits[i]
            ctr *= 10
        num += 1
        result = []
        for i in str(num):
            result.append(int(i))
        return result