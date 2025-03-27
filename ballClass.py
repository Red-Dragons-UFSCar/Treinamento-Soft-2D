class Ball:
    def __init__(self):
        self.xPos = 0  # Posição x no campo
        self.yPos = 0  # Posição y no campo

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
