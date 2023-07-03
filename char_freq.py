class Solution:
    def frequencySort(self, s: str) -> str:
        s_sort = sorted(s)
        s_dict = {}
        ctr = 0
        curr = s_sort[0]
        for i in range(len(s_sort)):
            if s_sort[i] == curr:
                ctr += 1
            else:
                s_dict[curr] = ctr
                curr = s_sort[i]
                ctr = 1 
                continue
        s_dict[curr] = ctr
        sorted_dict = dict(sorted(s_dict.items(), key = lambda x:x[1], reverse = True))
        ans = ""
        for a in sorted_dict.keys():
            ans += a*sorted_dict[a]
        return ans
