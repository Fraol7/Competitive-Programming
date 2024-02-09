class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        prefix = {}
        for i, num in enumerate(nums):
            if num in prefix:
                prefix[num][0] += 1
                prefix[num][1].append(prefix[num][1][-1] + i)
            else:
                prefix[num] = [1, [i]]
        arr = []
        for i, num in enumerate(nums):
            if len(prefix[num][1]) == 1:
                arr.append(0)
            else:
                presum = prefix[num][1]
                n = len(prefix[num][1])
                k = n - prefix[num][0]
                mid = (2*k - n + 1)*i
                left = presum[k] - i
                right = presum[-1] - presum[k]
                arr.append(right-left+mid)
                prefix[num][0] -= 1
        return arr
