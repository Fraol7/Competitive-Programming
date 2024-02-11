class Solution:
    def bestClosingTime(self, customers: str) -> int:
        arr_of_cust = []
        for i in customers:
            if i == 'Y':
                arr_of_cust.append(0)
            else:
                arr_of_cust.append(1)
        prefix = [0]
        for k in range(len(customers)):
            prefix.append(prefix[-1]+arr_of_cust[k])
        zeros = arr_of_cust.count(0)
        penalty, min_pen = 0, float('inf')
        hrs = 0
        for j in range(len(customers)+1):
            penalty = prefix[j] + zeros - (j - prefix[j])
            if penalty < min_pen:
                min_pen = penalty
                hrs = j
        return hrs