class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = 0
        count = {'T':0, 'F':0}
        max_len = 0
        for j in range(len(answerKey)):
            count[answerKey[j]] += 1
            while count['F'] > k and count['T'] > k:
                count[answerKey[i]] -= 1
                i += 1
            max_len = max(max_len, j-i+1)
        return max_len