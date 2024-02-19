class Solution:
    def isValid(self, s: str) -> bool:
        refer = {')':'(', ']':'[', '}':'{'}
        stack = []
        for brak in s:
            if brak not in refer:
                stack.append(brak)
            elif stack and stack[-1] != refer[brak]:
                return False
            elif not stack:
                return False
            else:
                stack.pop()
        return True if not stack else False
                
        