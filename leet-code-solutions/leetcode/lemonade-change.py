class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        refer = defaultdict(int)
        for cash in bills:
            if cash == 20:
                refer[20] += 1
                if refer[5] >= 1 and refer[10] >= 1:
                    refer[5] -= 1
                    refer[10] -= 1
                elif refer[5] >= 3:
                    refer[5] -= 3
                else: 
                    return False
            elif cash == 10:
                refer[10] += 1
                if refer[5] >= 1:
                    refer[5] -= 1
                else:
                    return False
            else:
                refer[5] += 1
        return True
            