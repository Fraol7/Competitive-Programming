class MyLinkedList:
    def __init__(self):
        self.List = []

    def get(self, index: int) -> int:
        if index > len(self.List) - 1:
            return -1
        return self.List[index]

    def addAtHead(self, val: int) -> None:
        self.List.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.List.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == len(self.List):
            self.addAtTail(val)
        elif index < len(self.List):
            self.List.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index > len(self.List) - 1:
            return None
        self.List.pop(index)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
