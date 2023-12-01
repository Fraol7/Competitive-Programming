class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            a = words[i]
            b = words[i+1]
            j, ctr = 0, 0
            while j < min(len(a),len(b)):
                if order.index(a[j]) == order.index(b[j]):
                    ctr += 1
                elif order.index(a[j]) < order.index(b[j]):
                    break
                elif order.index(a[j]) > order.index(b[j]):
                    return False

                j += 1
            if ctr == len(b) and len(a) > len(b): return False
        return True