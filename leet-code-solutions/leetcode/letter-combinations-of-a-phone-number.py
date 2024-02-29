class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        self.result = []
        self.refer = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def helper(digits, combined):
            if len(digits) == 0:
                self.result.append(combined)
                return
            temp = self.refer[digits[0]]
            for i in temp:
                helper(digits[1:], combined+i)
        helper(digits, '')
        return self.result

        