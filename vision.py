import numpy as np

class Vision:

    def getPoseRobot(self):
       x_robot = np.random.uniform(0,150)
       y_robot = np.random.uniform(0,130)
       theta = np.random.uniform (-np.pi, np.pi)
       return (x_robot, y_robot, theta)
    
    def getPoseBall(self):
        x_ball = np.random.uniform(0,150)
        y_ball = np.random.uniform(0,130)
        return (x_ball, y_ball)