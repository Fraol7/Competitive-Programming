class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mini_stack = []
        score = 0
        for idx,num in enumerate(arr):
            while mini_stack and mini_stack[-1][0] > num:
                right = idx-mini_stack[-1][1]
                last_num, last_idx = mini_stack.pop()
                if mini_stack:
                    left = last_idx-mini_stack[-1][1]
                else:
                    left = last_idx + 1
                score += left*right*last_num
            mini_stack.append((num, idx))
        while mini_stack:
            right = len(arr)-mini_stack[-1][1]
            last_num, last_idx = mini_stack.pop()
            if mini_stack:
                left = last_idx-mini_stack[-1][1]
            else:
                left = last_idx + 1
            score += left*right*last_num
        return score%(10**9 + 7)
