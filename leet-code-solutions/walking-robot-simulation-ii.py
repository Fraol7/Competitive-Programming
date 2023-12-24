class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.direct = "East"
        self.start = [0,0]
        self.arr = [width-1,height-1]

    def step(self, num: int) -> None:
        total = ((self.height+self.width-2)*2)
        num %= total
        if num != 0:
           i = 0
           while i < num:
                if self.direct == "East":
                    if self.start[0] == self.width-1:
                        num += 1
                        self.direct = "North"
                    else:
                        self.start[0] += 1

                elif self.direct == "West":
                    if self.start[0] == 0:
                        num += 1
                        self.direct = "South"
                    else:
                        self.start[0] -= 1
                elif self.direct == "North":
                    if self.start[1] == self.height - 1:
                        num += 1
                        self.direct = "West"
                    else:
                        self.start[1] += 1
                elif self.direct == "South":
                    if self.start[1] == 0:
                        num += 1
                        self.direct = "East"
                    else:
                        self.start[1] -= 1
                i += 1      
        elif self.start == [0,0]  and self.direct == "East":
            self.direct = "South"
      
    def getPos(self) -> List[int]:
        return self.start

    def getDir(self) -> str:
        return self.direct


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()