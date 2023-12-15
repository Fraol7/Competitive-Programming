class FrequencyTracker:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.has = defaultdict(int)
    def add(self, number: int) -> None:
        n = self.frequency[number]
        self.has[n] -= 1
        self.frequency[number] += 1
        self.has[n + 1] += 1

    def deleteOne(self, number: int) -> None:
        if self.frequency[number] != 0:
            n = self.frequency[number]
            self.has[n] -= 1
            self.frequency[number] -= 1
            self.has[self.frequency[number]] += 1
    def hasFrequency(self, frequency: int) -> bool:
        return True if self.has[frequency] != 0 else False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)