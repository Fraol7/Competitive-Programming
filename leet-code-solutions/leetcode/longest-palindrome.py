class Solution:
    def longestPalindrome(self, s: str) -> int:
        refer = Counter(s)
        flag = False
        longest = 0
        for value in refer.values():
            if value%2 == 1:
                flag = True
            longest += value//2
        longest *= 2
        if flag:
            longest += 1
        return longest
