class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open, close = n, n
        self.bracket = []
        def helper(open, close, temp):
            if close == 0:
                self.bracket.append(temp)
                return
            if close == open:
                helper(open-1, close, temp+'(')
            elif close > open and open > 0:
                helper(open, close-1, temp+')')
                helper(open-1, close, temp+'(')
            elif close > open and open == 0:
                helper(open, close-1, temp+')')
        helper(open, close, '')
        return self.bracket
