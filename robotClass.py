class Robot:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.theta = 0
        self.L = 7.5
        self.R = 3.5
    
    def setXPos(self, xPos):
        self.xPos = xPos
    
    def setYPos(self, yPos):
        self.yPos = yPos

    def setTheta(self, theta):
        self.theta = theta

    def setL(self, L):
        self.L = L

    def setR(self, R):
        self.R = R

    def getXPos(self):
        return self.xPos
    
    def getYPos(self):
        return self.yPos
    
    def getTheta(self):
        return self.theta
    
    def getL(self):
        return self.L
    
    def getR(self):
        return self.R
    
    def setPose(self, x, y, theta):
        self.xPos = x
        self.yPos = y
        self.theta = theta