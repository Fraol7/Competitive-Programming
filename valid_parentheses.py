class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_tags = ["]","}",")"]
        openning_tags = ["[","{","("]
        for i in s:
            if i in openning_tags:
                stack.append(i)
            if i in closing_tags:
                if stack[-1] == openning_tags[closing_tags.index(i)]:
                    stack.pop()
                else:
                    return False
        return stack == []
