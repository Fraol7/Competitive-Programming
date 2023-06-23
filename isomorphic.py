class Solution(object):
    def isIsomorphic(self, s, t):
        maps = []
        mapt = []
        for idx in s:
            maps.append(s.index(idx))
        for idx in t:
            mapt.append(t.index(idx))
        if maps == mapt:
            return True
        return False
