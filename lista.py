import numpy as np

############################## Exercício 1 ######################################################################################

def calcular_media(a, b):
    return (a + b) / 2

resultado_media = calcular_media(5, 3)
print(f'Média de 5 e 3 é: {resultado_media}\n')





############################## Exercício 2 ######################################################################################
def rotacionar_vetor(vetor, angulo):
    matriz_rotacao = [
        [np.cos(angulo), -np.sin(angulo)],   
        [np.sin(angulo), np.cos(angulo)]
    ]
    
    vetor_rotacionado = np.dot(matriz_rotacao, vetor)
    return vetor_rotacionado

# Vetor a ser rotacionado
vetor_inicial = np.array([[0, 1],
                          [0, 1]])

# Ângulo de rotação de 45 graus
angulo_rotacao = np.pi / 4  

vetor_resultante = rotacionar_vetor(vetor_inicial, angulo_rotacao)

angulo_inicial = np.arctan2(vetor_inicial[1], vetor_inicial[0])
angulo_final = np.arctan2(vetor_resultante[1], vetor_resultante[0])
diferenca_angulos = angulo_final - angulo_inicial

print(f'antes da rotação: {np.degrees(angulo_inicial)}°')
print(f'depois da rotação: {np.degrees(angulo_final)}°')
print(f'Diferença entre eles: {np.degrees(diferenca_angulos)}°\n')



############################## Exercício 3 ######################################################################################
def projetar_ponto_circunferencia(ponto, raio, centro):
    x, y = ponto
    a, b = centro
    
    x_mov = x - a
    y_mov = y - b
    
    # Calcula o ângulo entre o ponto movido e a origem
    angulo = np.arctan2(y_mov, x_mov)

    x_proj = raio * np.cos(angulo)
    y_proj = raio * np.sin(angulo)
    

    x_proj += a
    y_proj += b
    
    return (x_proj, y_proj)

# Definindo o raio e o centro da circunferência
raio = 1  
centro = (0, 0)  
ponto_inicial = (1, 0)

# Calculando a projeção do ponto na circunferência
ponto_projetado = projetar_ponto_circunferencia(ponto_inicial, raio, centro)
print(f'Ponto original: {ponto_inicial}')
print(f'Ponto projetado na circunferência: {ponto_projetado}')

