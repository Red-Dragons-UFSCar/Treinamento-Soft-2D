import numpy as np

def media(a, b):
    return (a + b) / 2

import numpy as np

def rotacionar_vetor(x, y, theta):
    theta_rad = np.radians(theta)  
    
    R = np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
                  [np.sin(theta_rad),  np.cos(theta_rad)]])
    
    vetor = np.array([x, y])
    
    vetor_rotacionado = np.dot(R, vetor)
    
    return vetor_rotacionado[0], vetor_rotacionado[1]

def projPontoCircunferencia(x, y, r=1, c1=0, c2=0):

    dx = x - c1
    dy = y - c2

    dist = np.sqrt(dx**2 + dy**2)

    x_proj = c1 + (dx / dist) * r
    y_proj = c2 + (dy / dist) * r

    return x_proj, y_proj

print("TESTE EXERCICIO 1")
resultado = media(4, 8)
print("Média:", resultado)  

print("TESTE EXERCICIO 2")
x_rot, y_rot = rotacionar_vetor(5, 3, 45)
print(f"Vetor rotacionado: ({x_rot:.2f}, {y_rot:.2f})")

print("TESTE EXERCICIO 3")
x_proj, y_proj = projPontoCircunferencia(2, 3)
print(f"Ponto projetado: ({x_proj:.2f}, {y_proj:.2f})")



