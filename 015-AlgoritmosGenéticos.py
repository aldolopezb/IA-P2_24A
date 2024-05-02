#Aldo López Barrios
#21310106
#--------------------------

import random

# Parámetros del algoritmo genético
TAMANO_POBLACION = 10
TAMANO_INDIVIDUO = 8
PROBABILIDAD_MUTACION = 0.1
NUM_GENERACIONES = 100

def inicializar_poblacion():
    return [[random.randint(0, 1) for _ in range(TAMANO_INDIVIDUO)] for _ in range(TAMANO_POBLACION)]

def evaluar_poblacion(poblacion):
    return [sum(individuo) for individuo in poblacion]

def seleccionar_padres(poblacion, valores_fitness):
    return random.choices(poblacion, weights=valores_fitness, k=2)

def cruzar(padre1, padre2):
    punto_corte = random.randint(1, TAMANO_INDIVIDUO - 1)
    hijo1 = padre1[:punto_corte] + padre2[punto_corte:]
    hijo2 = padre2[:punto_corte] + padre1[punto_corte:]
    return hijo1, hijo2

def mutar(individuo):
    for i in range(len(individuo)):
        if random.random() < PROBABILIDAD_MUTACION:
            individuo[i] = 1 - individuo[i]
    return individuo

# Algoritmo genético
poblacion = inicializar_poblacion()
for _ in range(NUM_GENERACIONES):
    valores_fitness = evaluar_poblacion(poblacion)
    nueva_poblacion = []
    for _ in range(TAMANO_POBLACION // 2):
        padre1, padre2 = seleccionar_padres(poblacion, valores_fitness)
        hijo1, hijo2 = cruzar(padre1, padre2)
        hijo1 = mutar(hijo1)
        hijo2 = mutar(hijo2)
        nueva_poblacion.extend([hijo1, hijo2])
    poblacion = nueva_poblacion

# Seleccionar el mejor individuo de la última generación
mejor_individuo = max(poblacion, key=lambda x: sum(x))
print("Mejor individuo encontrado:", mejor_individuo)
print("Fitness del mejor individuo:", sum(mejor_individuo))
