class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans  = []
        def bt(res,check) :
            if len(res) == len(nums) :
                ans.append(res[:])
                return
            
            for i in nums :
                if i not in check :
                    check.add(i)
                    res.append(i)
                    bt(res,check)
                    res.remove(i)
                    check.remove(i)
        bt([],set())
        return ans
