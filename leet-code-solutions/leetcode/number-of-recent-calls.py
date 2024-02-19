class RecentCounter:
    def __init__(self):
        self.recent = deque()
    def ping(self, t: int) -> int:
        self.recent.append(t)
        for i in list(self.recent):
            if i < t-3000:
                self.recent.popleft()
        return len(self.recent)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)