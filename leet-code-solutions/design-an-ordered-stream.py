class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.alist = [None]*n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        result = []
        self.alist[idKey-1] = value
        while self.pointer < self.n and self.alist[self.pointer]:
            result.append(self.alist[self.pointer])
            self.pointer += 1
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)