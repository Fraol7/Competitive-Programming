class MyQueue(object):
    def __init__(self):
        self.stack = []
        self.queue = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        self.peek()
        return self.queue.pop()
    def peek(self):
        if not self.queue:
            while self.stack:
                self.queue.append(self.stack.pop())
        return self.queue[-1]
    def empty(self):
        return not self.stack and not self.queue
