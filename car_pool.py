class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        for trip in trips:
            minHeap.extend([(trip[1], trip[0]), (trip[2], -trip[0])])
        heapify(minHeap)
        while capacity >= 0 and minHeap:
            capacity -= heappop(minHeap)[1]
        return len(minHeap) == 0
