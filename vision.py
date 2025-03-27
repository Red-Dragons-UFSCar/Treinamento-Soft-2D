class Vision:
    def getPoseRobot(self):
        x = random.uniform(0, 150)  
        y = random.uniform(0, 130)  
        theta = random.uniform(-np.pi, np.pi)  # θ entre -π e π
        return x, y, theta

    def getPoseBall(self):
        x = random.uniform(0, 150)  
        y = random.uniform(0, 130)  
        return x, y
