class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.unflipped = ["0"] * self.size 
        self.flipped = ["1"] * self.size 
        self.ctrOne = 0

    def fix(self, idx: int) -> None:
        if self.unflipped[idx] != "1":
            self.unflipped[idx] = "1"
            self.flipped[idx] = "0"
            self.ctrOne += 1

    def unfix(self, idx: int) -> None:
        if self.unflipped[idx] != "0":
            self.unflipped[idx] = "0"
            self.flipped[idx] = "1"
            self.ctrOne -= 1

    def flip(self) -> None:
        self.unflipped, self.flipped = self.flipped, self.unflipped
        self.ctrOne = self.size  - self.ctrOne

    def all(self) -> bool:
        return self.size == self.ctrOne

    def one(self) -> bool:
        return self.ctrOne > 0

    def count(self) -> int:
        return self.ctrOne

    def toString(self) -> str:
        return "".join(self.unflipped)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()