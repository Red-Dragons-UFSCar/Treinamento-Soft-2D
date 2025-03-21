class Robot:
    def __init__(self):
        self.L = 7.5
        self.R = 3.5
        self.xPos = 0
        self.yPos = 0
        self.theta = 0
    
    # getters and setters
    def get_L(self):
        return self.L
    def set_L(self, L):
        self.L = L
        
    def get_R(self):
        return self.R
    def set_R(self, R):
        self.R = R
        
    def get_xPos(self):
        return self.xPos
    def set_xPos(self, x):
        self.xPos = x

    def get_yPos(self):
        return self.yPos
    def set_yPos(self, y):
        self.yPos = y

    def get_theta(self):
        return self.theta
    def set_theta(self, theta):
        self.theta = theta

    # setar a posição do robô
    def setPose(self, x, y, theta):
        self.set_xPos(x)
        self.set_yPos(y)
        self.set_theta(theta)
        