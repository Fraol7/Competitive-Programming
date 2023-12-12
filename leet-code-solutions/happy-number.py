class Solution:
    def isHappy(self, n: int) -> bool:
        freq = defaultdict(int)
        while n not in freq:
            num = 0
            for i in str(n):
                num += int(i)**2
            if num == 1:
                return True
            freq[n] = 1
            n = num