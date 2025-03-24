import numpy as np
import math

def f_media (a,b):
    media = (a+b)/2
    return media

def rotacionar(x1, y1, angulo_graus):
    angulo_rad = math.radians(angulo_graus)
    
    R = np.zeros ([2,2])
    R [0] [0] = math.cos(angulo_rad)
    R [0] [1] = -math.sin(angulo_rad)
    R [1] [0] = math.sin(angulo_rad)
    R [1] [1] = math.cos(angulo_rad)

    X = np.zeros ([2,1])
    X [0] [0] = x1
    X [1] [0] = y1
    
    V = np.dot (R,X)
    V = np.round(V, decimals=6)

    anguloRotacao = np.arctan2(V[1], V[0])

    if (anguloRotacao == angulo_rad):
        return V
    else:
        return -1
    
#x1 = 1
#y1 = 0
#angulo_graus = 90
#vetor_rotacionado = rotacionar(x1, y1, angulo_graus)
#print(vetor_rotacionado)

def projPontoCircunferencia(x,y,c1,c2, r):
    x_deslocado = x - c1
    y_deslocado = y - c2
    
    distancia = math.sqrt(x_deslocado**2 + y_deslocado*2)
    
    x_projecao = (x_deslocado/distancia)*r+c1
    y_projecao = (y_deslocado/distancia)*r+c2
    
    return (x_projecao, y_projecao)