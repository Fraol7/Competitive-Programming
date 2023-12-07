class Solution:
    def largestOddNumber(self, num: str) -> str:
        while num:
            anum = int(num[-1])
            if anum%2 == 0:
                num = num[:-1]
            else:
                return num
        return ""