class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        new=Counter(arr)
        n=len(arr)
        count=0
        ans=0
        new=sorted(new.values())[::-1]
        for i in new:
            count+=i
            ans+=1
            if count>=n//2:
                return ans
