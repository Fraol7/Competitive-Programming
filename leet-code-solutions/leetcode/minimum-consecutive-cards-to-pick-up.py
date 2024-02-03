class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ctr_dict = defaultdict(tuple)
        for i in range(len(cards)):
            if cards[i] not in ctr_dict:
                ctr_dict[cards[i]] = (0, i)
            else:
                if ctr_dict[cards[i]][0] == 0:
                    ctr_dict[cards[i]] = (i - ctr_dict[cards[i]][1] + 1, i)
                else:
                    ctr_dict[cards[i]] = (min(ctr_dict[cards[i]][0], i - ctr_dict[cards[i]][1] + 1), i)
        ctr = float('inf')
        for j in ctr_dict.values():
            if j[0] == 0:
                continue
            ctr = min(ctr, j[0])
        if ctr == float('inf'):
            return -1
        return ctr