class Ball:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0
    
    def getXPos(self):
        return self.xPos
    def setXPos(self, xPos):
        self.xPos = xPos

    def getYPos(self):
        return self.yPos
    def setYPos(self, yPos):
        self.yPos = yPos
    
    def setPose(self, x, y):
        self.xPos = x
        self.yPos = y 
