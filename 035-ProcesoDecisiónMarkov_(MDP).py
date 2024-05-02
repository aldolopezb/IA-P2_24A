#Aldo López Barrios
#21310106
#--------------------------

import numpy as np

# Definir el MDP
num_estados = 3
num_acciones = 2
num_iteraciones = 100
gamma = 0.9  # Factor de descuento

# Matriz de recompensas R(s, a)
recompensas = np.array([
    [1, -1],
    [2, 0],
    [0, 1]
])

# Matriz de transiciones T(s, a, s')
transiciones = np.array([
    [[0.8, 0.2, 0.0],
     [0.1, 0.7, 0.2],
     [0.0, 0.3, 0.7]],
    
    [[0.6, 0.4, 0.0],
     [0.0, 0.8, 0.2],
     [0.0, 0.0, 1.0]]
])

# Iteración de valores para calcular los valores óptimos
valores = np.zeros(num_estados)
for _ in range(num_iteraciones):
    nuevos_valores = np.zeros(num_estados)
    for estado in range(num_estados):
        valores_acciones = []
        for accion in range(num_acciones):
            valor_accion = 0
            for nuevo_estado in range(num_estados):
                valor_accion += transiciones[accion][estado][nuevo_estado] * (recompensas[estado][accion] + gamma * valores[nuevo_estado])
            valores_acciones.append(valor_accion)
        nuevos_valores[estado] = max(valores_acciones)
    valores = nuevos_valores

print("Valores óptimos:", valores)
