class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n = max(len(word1), len(word2))
        w1 = ''.join(word1)
        w2 = ''.join(word2)
        if w1 == w2: return True
        return False
        