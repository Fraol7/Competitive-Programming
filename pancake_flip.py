class Solution(object):
    def pancakeSort(self, arr):
        ans = []
        end = len(arr)
        while end > 0:
            maxi = max(arr[:end])
            max_index = arr[:end].index(maxi)
            k = max_index+1
            if k == end:
                end -= 1
            else:
                ans.append(k)
                arr[:k] = arr[:k][::-1]
                ans.append(end)
                arr[:end] = arr[:end][::-1]
                end -= 1
        return ans
