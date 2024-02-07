class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        interval = [0]*(len(nums)+1)
        for start, end in requests:
            interval[start] += 1
            interval[end+1] -= 1
        prefix = [interval[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]+interval[i])
        prefix.sort(reverse=True)
        nums.sort()
        ans = 0
        for aval in prefix:
            ans += (aval*nums.pop())%(10**9+7)
        return ans%(10**9+7)

