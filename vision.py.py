import numpy as np

class Vision:
    def getPoseRobot(self):
        x = np.random.uniform(0, 150)
        y = np.random.uniform(0, 130)
        theta = np.random.uniform(-np.pi, np.pi)
        return x, y, theta

    def getPoseBall(self):
        x = np.random.uniform(0, 150)
        y = np.random.uniform(0, 130)
        return x, y