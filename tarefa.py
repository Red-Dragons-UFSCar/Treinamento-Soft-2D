import numpy as np
import random
import math

def f_media (a,b):
    media = (a+b)/2
    return media


def rotacionar(x1, y1, ang):
    angulo = math.radians(ang)
    R = np.zeros ([2,2])
    X = np.zeros ([2,1])
    
    R [0] [0] = math.cos(angulo)
    R [0] [1] = -math.sin(angulo)
    R [1] [0] = math.sin(angulo)
    R [1] [1] = math.cos(angulo)
    
    X [0] [0] = x1
    X [1] [0] = y1
    
    V = np.dot (R,X)
    return V

#def projecao(x,y,c1,c2):
    
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