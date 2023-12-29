class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        refer = Counter(nums)
        n = len(refer)-1
        ctr = 0
        for i in refer:
            ctr += refer[i]*n
            n -= 1
        return ctr