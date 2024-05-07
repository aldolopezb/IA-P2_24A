#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
import pymc3 as pm

# Datos de transición de la cadena de Markov
transiciones = np.array([[0.7, 0.2, 0.1],
                         [0.1, 0.6, 0.3],
                         [0.2, 0.3, 0.5]])

# Inicialización del estado inicial
estado_inicial = np.array([0.5, 0.3, 0.2])

# Crear un modelo de cadenas de Markov utilizando pymc3
with pm.Model() as modelo:
    # Definir la matriz de transición como una variable estocástica
    P = pm.Dirichlet('P', a=np.ones_like(transiciones[0]), shape=(3, 3))
    
    # Definir el estado inicial como una variable estocástica
    estado = pm.Dirichlet('estado', a=estado_inicial)
    
    # Generar la secuencia de estados utilizando el método de Monte Carlo
    secuencia_estados = [estado]
    for _ in range(10):  # Simular 10 pasos de la cadena de Markov
        estado = pm.Categorical(f'estado_{_}', p=estado.dot(P), shape=3)
        secuencia_estados.append(estado)
    
    # Observar la secuencia de estados
    observaciones = pm.sample_prior_predictive(samples=1)

# Imprimir las secuencias de estados generadas
print("Secuencias de estados generadas:")
for i, estado in enumerate(secuencia_estados):
    print(f"Paso {i}: {observaciones[f'estado_{i}'][0]}")
