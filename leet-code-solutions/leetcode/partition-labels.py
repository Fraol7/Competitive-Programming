class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        refer, parts = {}, []
        for i in range(len(s)):
            if s[i] in refer:
                refer[s[i]][1] = max(refer[s[i]][1], i)
            else:
                refer[s[i]] = [i, i]
        pairs = [pair for pair in refer.values()]
        left, right = pairs[0][0], pairs[0][1]
        for i in range(1,len(pairs)):
            pair = pairs[i]
            if right > pair[0]:
                right = max(right, pair[1])
            else:
                parts.append(right-left+1)
                left, right = pair[0], pair[1]
        parts.append(right-left+1)
        return parts
