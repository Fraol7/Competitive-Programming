class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = {}
        res = 0
        for t in time:
            r = t % 60
            if r in freq.keys():
                freq[r] += 1
            else:
                freq[r] = 1

        for k, v in freq.items():
            if k == 0 or k == 30:
                res += (v * (v - 1)) // 2
            elif k <= 29 and 60 - k in freq.keys():
                res += v * freq[60 - k]

        return res
