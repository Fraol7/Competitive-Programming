class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = ""
        for i in s:
            if i.isalnum(): 
                _s += i.lower()
        rev_s = ""
        end = len(_s) - 1
        while end >= 0:
            rev_s += _s[end]
            end -= 1
        if rev_s == _s:
            return True
        return False