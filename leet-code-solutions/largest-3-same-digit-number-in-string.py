class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = []
        for i in range(len(num)-2):
            if len(set(num[i:i+3])) == 1:
                res.append(num[i])
        if res: return max(res)*3
        return ''
        