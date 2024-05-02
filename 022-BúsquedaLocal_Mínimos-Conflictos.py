#Aldo López Barrios
#21310106
#--------------------------

import random

def minimos_conflictos(CSP, max_iter):
    asignacion = asignacion_inicial(CSP)
    for _ in range(max_iter):
        if es_solucion(asignacion, CSP):
            return asignacion
        variable = seleccionar_variable_conflictiva(asignacion, CSP)
        valor = seleccionar_valor_conflictivo(variable, asignacion, CSP)
        asignacion[variable] = valor
    return None

def asignacion_inicial(CSP):
    return {variable: random.choice(valores) for variable, valores in CSP.items()}

def es_solucion(asignacion, CSP):
    for var, val in asignacion.items():
        if not cumple_restricciones(var, val, asignacion, CSP):
            return False
    return True

def seleccionar_variable_conflictiva(asignacion, CSP):
    variables_conflictivas = []
    for variable in CSP:
        if not cumple_restricciones(variable, asignacion[variable], asignacion, CSP):
            variables_conflictivas.append(variable)
    return random.choice(variables_conflictivas)

def seleccionar_valor_conflictivo(variable, asignacion, CSP):
    return random.choice(CSP[variable])

def cumple_restricciones(variable, valor, asignacion, CSP):
    # Verificar si la asignación cumple con las restricciones del CSP
    # En este ejemplo, asumimos que todas las restricciones son satisfechas
    return True

# Ejemplo de uso
CSP = {
    'A': [1, 2, 3],
    'B': [1, 2],
    'C': [2, 3]
}
max_iter = 1000

solucion = minimos_conflictos(CSP, max_iter)
if solucion is not None:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")
