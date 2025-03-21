class Ball:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0

    # getters and setters
    def get_xPos(self):
        return self.xPos
    def set_xPos(self, x):
        self.xPos = x

    def get_yPos(self):
        return self.yPos
    def set_yPos(self, y):
        self.yPos = y
        
    # setar coordenadas da bola
    def setPose(self, x, y):
        self.set_xPos(x)
        self.set_yPos(y)

