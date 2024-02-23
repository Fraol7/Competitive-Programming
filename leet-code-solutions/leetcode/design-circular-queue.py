class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.bot, self.top = -1, 0
        self.queue = [None]*k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.bot = (self.bot + 1)%self.k
        self.queue[self.bot] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.top] = None
        self.top = (self.top + 1)%self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.top]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.bot] 

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()