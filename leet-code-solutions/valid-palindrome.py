class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = ""
        for i in s:
            if i.isalnum():
                _s += i.lower()
        left, right = 0, len(_s)-1
        while left < right:
            if _s[left] != _s[right]:
                return False
            left += 1
            right -= 1
        return True