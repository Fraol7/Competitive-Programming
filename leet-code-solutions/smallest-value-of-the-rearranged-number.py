class Solution:
    def smallestNumber(self, num: int) -> int:
        num = str(num)
        if num[0] =='-':
            num1 = sorted(num[1:], reverse=True)
            num = ['-']+num1
        else:
            num = sorted(num)
            zeros = num.count("0")
            if zeros == len(num): return 0
            if num[0] == "0":
                num[0], num[zeros] = num[zeros], num[0]
        return int(''.join(num))