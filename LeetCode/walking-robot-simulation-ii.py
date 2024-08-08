class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.direction = 'East'
        self.coordinate = [0,0]
        self.per = (self.height-1)*2+(self.width-1)*2
    def step(self, num: int) -> None:
        if self.coordinate == [0,0] and num%(self.per) == 0:
            self.direction = 'South'
        for i in range(num%(self.per)):
            if self.direction == 'East' and self.coordinate[0] < self.width-1:
                self.coordinate[0] +=1
            elif self.direction == 'East' and self.coordinate[0] == self.width-1:
                self.direction = 'North'
                self.coordinate[1] +=1
            elif self.direction == 'West' and self.coordinate[0] > 0:
                self.coordinate[0] -=1
            elif self.direction == 'West' and self.coordinate[0] == 0:
                self.direction = 'South'
                self.coordinate[1] -=1
            elif self.direction == 'North' and self.coordinate[1] < self.height-1:
                self.coordinate[1] +=1
            elif self.direction == 'North' and self.coordinate[1] == self.height-1:
                self.direction = 'West'
                self.coordinate[0] -=1
            elif self.direction == 'South' and self.coordinate[1] > 0:
                self.coordinate[1] -=1
            elif self.direction == 'South' and self.coordinate[1] == 0:
                self.direction = 'East'
                self.coordinate[0] +=1                  
    def getPos(self) -> list[int]:
        return self.coordinate
    def getDir(self) -> str:
        return self.direction
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()