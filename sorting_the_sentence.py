class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)-1):
            place_index = i
            for j in range(i+1, len(s)):
                if s[j][-1] < s[place_index][-1]:
                    place_index = j
            s[place_index], s[i] = s[i], s[place_index]
        sentence = ""
        for i in s:
            for j in i[:-1]:
                sentence += j
            if s[-1] != i:
                sentence += " "
        return sentence
