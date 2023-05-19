class Solution:
    def topKFrequent(self, nums, k):
        ans = {}
        for i in nums:
            if i not in ans:
                ans[i]=1
            else:
                ans[i]+=1
        sortedAns = dict(sorted(ans.items(), key=lambda x:x[1], reverse=True))
        result = []
        for j in sortedAns:
            result.append(j)
        return result[:k]
