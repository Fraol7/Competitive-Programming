class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        stack = []
        ans = [0]*len(temp)
        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans


