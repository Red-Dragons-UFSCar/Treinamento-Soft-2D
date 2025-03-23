import numpy as np
import math

def f_media (a,b):
    media = (a+b)/2
    return media


def rotacionar(x1, y1, angulo):
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
    