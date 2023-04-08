class Solution:
    def recur(self, a):
        if a == 1:
            return 0
        else:
            return (a-1) + self.recur(a-1)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        visited = []
        ctr = 0
        temp = []
        for i in nums:
            if i in visited:
                continue
            else:
                for j in nums:
                    if i == j:
                        ctr += 1
                visited.append(i)
            temp.append(ctr)
            ctr = 0
        answer = 0
        for k in temp:
            answer += self.recur(k)
        return answer
