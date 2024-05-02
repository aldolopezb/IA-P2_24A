#Aldo López Barrios
#21310106
#--------------------------

from collections import Counter
import math

def gini_impureza(etiquetas):
    """
    Calcula la impureza de Gini para un conjunto de etiquetas.
    """
    total_muestras = len(etiquetas)
    conteo_clases = Counter(etiquetas)
    impureza = 1
    for clase in conteo_clases:
        probabilidad_clase = conteo_clases[clase] / total_muestras
        impureza -= probabilidad_clase ** 2
    return impureza

def ganancia_informacion(conjunto_total, subconjuntos):
    """
    Calcula la ganancia de información para un conjunto total dado y sus subconjuntos.
    """
    impureza_total = gini_impureza(conjunto_total)
    total_muestras = len(conjunto_total)
    ganancia = impureza_total
    for subconjunto in subconjuntos:
        proporción = len(subconjunto) / total_muestras
        ganancia -= proporción * gini_impureza(subconjunto)
    return ganancia

# Ejemplo de datos de entrenamiento (características y etiquetas)
caracteristicas = [
    [5, 2],
    [4, 3],
    [6, 1],
    [5, 4],
    [4, 2]
]
etiquetas = ['A', 'B', 'A', 'B', 'A']

# Calcular la ganancia de información para cada característica
ganancias = []
for i in range(len(caracteristicas[0])):
    valores_caracteristica = [fila[i] for fila in caracteristicas]
    conjunto_total = etiquetas
    subconjuntos = [[etiquetas[j] for j in range(len(valores_caracteristica)) if valores_caracteristica[j] == valor]
                    for valor in set(valores_caracteristica)]
    ganancia = ganancia_informacion(conjunto_total, subconjuntos)
    ganancias.append(ganancia)

# Mostrar las ganancias de información para cada característica
for i, ganancia in enumerate(ganancias):
    print(f"Ganancia de información para la característica {i+1}: {ganancia}")
