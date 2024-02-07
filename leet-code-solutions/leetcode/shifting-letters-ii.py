class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shifting_values = [0]*(len(s)+1)
        for shift in shifts:
            k = 1
            if shift[2] == 0:
                k = -1
            shifting_values[shift[0]] += k
            shifting_values[shift[1]+1] -= k
        prefix_shift = [shifting_values[0]]
        for i in range(1, len(s)+1):
            prefix_shift.append(prefix_shift[-1] + shifting_values[i])
        result = []
        for j in range(len(s)):
            result.append(chr((ord(s[j])-ord('a') + prefix_shift[j])%26 + ord('a')))
        return ''.join(result)
