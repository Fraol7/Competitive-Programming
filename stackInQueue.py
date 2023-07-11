class MyStack:
    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []

    def push(self, x: int) -> None:
        self.queue_2.append(x)
        while len(self.queue_1) > 0:
            self.queue_2.append(self.queue_1.pop(0))
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1

    def pop(self) -> int:
        return self.queue_1.pop(0)

    def top(self) -> int:
        return self.queue_1[0]

    def empty(self) -> bool:
        return len(self.queue_1) == 0
