class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = ""
        for i in s:
            if i.isalnum(): 
                _s += i.lower()
        rev_s = _s[::-1]
        if rev_s == _s:
            return True
        return False
