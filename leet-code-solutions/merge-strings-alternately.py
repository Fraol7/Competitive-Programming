class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        n = min(len1, len2)
        merge = ''
        for i in range(n):
            merge += word1[i]
            merge += word2[i]
        if len1 > len2:
            merge += word1[n:]
        elif len1 < len2:
            merge += word2[n:]
        return merge
