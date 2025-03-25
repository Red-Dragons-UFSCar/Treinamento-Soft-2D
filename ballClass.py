class Ball:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0

    def get_xPos(self):
        return self.xPos

    def set_xPos(self, x):
        self.xPos = x

    def get_yPos(self):
        return self.yPos

    def set_yPos(self, y):
        self.yPos = y

    def setPose(self, x, y):
        self.xPos = x
        self.yPos = y