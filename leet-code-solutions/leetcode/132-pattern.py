class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mini = 10**9
        min_dict = {}
        for i,num in enumerate(nums):
            min_dict[i] = mini
            mini = min(mini, num)
        stack = []
        for i,num in enumerate(nums):
            if not stack:
                stack.append((i, num))
            elif stack[-1][1] <= num:
                while stack and stack[-1][1] <= num:
                    stack.pop()
                if stack and min_dict[stack[-1][0]] < num:
                    return True
                stack.append((i, num))
            elif stack[-1][1] > num:
                if stack and min_dict[stack[-1][0]] < num:
                    return True
                stack.append((i, num))
        return False

