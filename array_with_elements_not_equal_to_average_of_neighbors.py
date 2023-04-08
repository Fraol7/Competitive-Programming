class Solution:
    def rearrangeArray(self, num: List[int]) -> List[int]:
        num.sort(reverse=True)
        num1 = num[:len(num)//2]
        num2 = num[len(num)//2:]
        for i in range(1, len(num), 2):
            num[i] = num1[i//2]
        for i in range(0, len(num), 2):
            num[i] = num2[i//2]
        return num
