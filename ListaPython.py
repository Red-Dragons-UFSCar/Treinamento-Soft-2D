import numpy as np

#Exercicio 1

def media(a,b):
    ans=(a+b)/2
    return ans


#Exercicio 2

def rotacionarVetores(vector,teta):
    R = [[np.cos(teta), -np.sin(teta)], 
         [np.sin(teta), np.cos(teta)]]
    newVector = np.dot(R, vector)
    return newVector


#Exercicio 3

def projPontoCircunferencia(x,y):
    if x != 0:
        m = y/x
        a = 1 + m**2 #ax**2 + bx + c = 0
        b = 0
        c = -1
        delta = b**2 -4*a*c

        if (delta<0):
            return None
    
        x1 = (-b + np.sqrt(delta))/(2*a)
        x2 = (-b - np.sqrt(delta))/(2*a)

        y1 = m*x1
        y2 = m*x2
    else:
        x1 = x
        x2 = x1 
        y1 = 1
        y2 = -1
    return (x1,y1),(x2,y2)


