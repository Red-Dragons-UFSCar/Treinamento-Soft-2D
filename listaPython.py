import numpy as np

### Exercício 1: função média
def media(a, b):
    return (a+b)/2

print(f'{media(5, 3)}\n')

### Exercício 2: função rotacionarVetores
def rotacionarVetores(X, theta):
    # matriz de rotação
    R = [[np.cos(theta), -np.sin(theta)],   
         [np.sin(theta), np.cos(theta)]]
    
    V = np.dot(R, X)
    return V

# vetor inicial
X = np.array([[0, 1],
              [0, 1]])

# rotação de 45 graus
theta = np.pi / 4  

V = rotacionarVetores(X, theta)

# ângulos antes e depois da rotação
ang_antes = np.arctan2(X[1], X[0])
ang_depois = np.arctan2(V[1], V[0])
dif_angulos = ang_depois - ang_antes

print(f'Ângulos antes da rotação: {np.degrees(ang_antes)}')
print(f'Ângulos depois da rotação: {np.degrees(ang_depois)}')
print(f"Diferênça: {np.degrees(dif_angulos)}\n")

### Exercício 3: função projPontoCircunferencia
def projPontoCircunferencia(ponto, raio, centro):
    x, y = ponto
    a, b = centro
    
    # mover ponto (centro na origem)
    x_mov = x - a
    y_mov = y - b
    
    # ângulo theta entre o ponto (movido) e a origem
    theta = np.arctan2(y_mov, x_mov)
    
    # projeção sobre a circunferência
    x_proj = raio * np.cos(theta)
    y_proj = raio * np.sin(theta)
    
    # voltar para a posição real
    x_proj = x_proj + a
    y_proj = y_proj + b
    
    return (x_proj, y_proj)

R = 1  
C = (0, 0)  
P = (1, 0)

# calculando projeção
p_proj = projPontoCircunferencia(P, R, C)
print(f'Ponto inicial: {P}')
print(f'Ponto projetado na circunferência: {p_proj}')
