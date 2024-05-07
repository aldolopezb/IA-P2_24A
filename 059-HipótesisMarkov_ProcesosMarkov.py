#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

# Definir la matriz de transición de estado
P = np.array([[0.8, 0.2],
              [0.1, 0.9]])

# Estado inicial
estado_inicial = np.array([0.5, 0.5])

# Función para generar una secuencia de estados usando el proceso de Markov
def generar_secuencia(P, estado_inicial, num_pasos):
    secuencia = [np.random.choice([0, 1], p=estado_inicial)]
    for _ in range(num_pasos - 1):
        estado_actual = secuencia[-1]
        proximo_estado = np.random.choice([0, 1], p=P[estado_actual])
        secuencia.append(proximo_estado)
    return secuencia

# Generar una secuencia de 10 estados
secuencia = generar_secuencia(P, estado_inicial, num_pasos=10)
print("Secuencia de estados:", secuencia)
