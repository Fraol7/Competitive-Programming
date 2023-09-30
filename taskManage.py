class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = dict()
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1
        heap = list()
        for task, count in counter.items():
            heappush(heap, (-count, task))
        time = 0
        while heap:
            temp = []
            for _ in range(n+1):
                if heap: 
                    temp.append((heappop(heap)))
            for count, task in temp:
                if count+1 < 0: 
                    heappush(heap, (count+1, task))
            time += len(temp) if not heap else n+1
                
        return time
