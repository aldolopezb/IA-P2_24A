#Aldo López Barrios
#21310106
#--------------------------

import re

from pulp import LpVariable, LpProblem, LpMinimize, lpSum, value

def acondicionamiento_corte(largos_materiales, demandas, largos_disponibles):
    # Crear el problema de programación lineal
    prob = LpProblem("Acondicionamiento del Corte", LpMinimize)

    # Crear variables de decisión
    x = LpVariable.dicts("Piezas", ((i, j) for i in range(len(largos_materiales)) for j in range(len(largos_disponibles))), lowBound=0, cat='Integer')

    # Definir la función objetivo
    prob += lpSum((largos_disponibles[j] - largos_materiales[i]) * x[(i, j)] for i in range(len(largos_materiales)) for j in range(len(largos_disponibles)))

    # Definir restricciones de demanda
    for i in range(len(largos_materiales)):
        prob += lpSum(x[(i, j)] for j in range(len(largos_disponibles))) * largos_materiales[i] >= demandas[i]

    # Resolver el problema
    prob.solve()

    # Obtener la solución
    solucion = {}
    for var in prob.variables():
        if var.varValue > 0:
            i, j = map(int, var.name.split('_')[1].split(','))
            solucion[f'Pieza {i + 1} en largo {largos_disponibles[j]}'] = var.varValue

    return solucion

# Ejemplo de uso
largos_materiales = [3, 5, 7]  # Longitudes de los materiales disponibles
demandas = [10, 20, 15]         # Demandas de cada tipo de pieza
largos_disponibles = [10, 15]   # Longitudes disponibles para cortar

solucion = acondicionamiento_corte(largos_materiales, demandas, largos_disponibles)
if solucion:
    print("Solución encontrada:")
    for pieza, cantidad in solucion.items():
        print(f"{pieza}: {cantidad} unidades")
else:
    print("No se encontró solución.")
