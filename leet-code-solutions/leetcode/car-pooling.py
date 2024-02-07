class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        destn = max([trip[-1] for trip in trips])
        travel = [0]*(destn+1)
        for num,start,end in trips:
            travel[start] += num
            travel[end] -= num
        prefix = [travel[0]]
        for i in range(1, destn+1):
            prefix.append(prefix[-1]+travel[i])
        return False if capacity < max(prefix) else True
