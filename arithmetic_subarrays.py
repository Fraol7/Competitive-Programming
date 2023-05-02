class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(r)):
            _l = l[i]
            _r = r[i]
            ListOfNums = nums[_l:_r+1]
            ListOfNums.sort()
            diff = ListOfNums[0] - ListOfNums[1]
            ctr = 0
            for j in range(len(ListOfNums)-1):
                if ListOfNums[j] - ListOfNums[j+1] == diff:
                    ctr += 1
            if ctr == len(ListOfNums)-1:
                answer.append(True)
            else:
                answer.append(False)
        return answer
