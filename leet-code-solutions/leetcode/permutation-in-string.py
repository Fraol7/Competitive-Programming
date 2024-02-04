class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ctr, w, match = Counter(s1), len(s1), 0     
        for i in range(len(s2)):
            if s2[i] in ctr:
                if not ctr[s2[i]]: match -= 1
                ctr[s2[i]] -= 1
                if not ctr[s2[i]]: match += 1
            if i >= w and s2[i-w] in ctr:
                if not ctr[s2[i-w]]: match -= 1
                ctr[s2[i-w]] += 1
                if not ctr[s2[i-w]]: match += 1
            if match == len(ctr):
                return True
        return False
        