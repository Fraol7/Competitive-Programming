class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_size = 1
        last = arr[0]
        curr_size = 1
        last_op = 0

        for n in arr[1:]:
            if n > last:
                if last_op != 2:
                    curr_size = 2
                else:
                    curr_size += 1
                last_op = 1
            elif n < last:
                if last_op != 1:
                    curr_size = 2
                else:
                    curr_size += 1
                last_op = 2
            else:
                curr_size = 1
                last_op = 0
            last = n
            max_size = max(curr_size,max_size)
        return max_size
