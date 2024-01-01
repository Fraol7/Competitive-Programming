class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        procTime = []
        largest = 0
        for i in range(0, len(tasks)-3, 4):
            procTime.append(max(tasks[i:i+4]))
        processorTime.sort(reverse=True)
        for i,j in zip(procTime, processorTime):
            largest = max(largest, i+j)
        return largest