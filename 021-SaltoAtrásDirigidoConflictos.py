#Aldo López Barrios
#21310106
#--------------------------

def salto_atras_dirigido_conflictos(CSP):
    asignacion = {}  # Inicializar una asignación vacía
    return buscar(asignacion, CSP)

def buscar(asignacion, CSP):
    if len(asignacion) == len(CSP):
        # Si la asignación está completa, devolverla como solución
        return asignacion
    
    variable = seleccionar_variable_sin_asignar(CSP, asignacion)
    for valor in ordenar_valores(CSP, variable):
        if consistente(asignacion, variable, valor, CSP):
            asignacion[variable] = valor
            resultado = buscar(asignacion, CSP)
            if resultado is not None:
                return resultado
            del asignacion[variable]
    return None

def seleccionar_variable_sin_asignar(CSP, asignacion):
    for variable in CSP:
        if variable not in asignacion:
            return variable

def ordenar_valores(CSP, variable):
    return CSP[variable]  # En este ejemplo, simplemente devolvemos los valores en el orden dado por el problema

def consistente(asignacion, variable, valor, CSP):
    # Verificar si el valor es consistente con las restricciones ya asignadas
    for var, val in asignacion.items():
        if not cumple_restriccion(var, val, variable, valor, CSP):
            return False
    return True

def cumple_restriccion(var1, val1, var2, val2, CSP):
    # Verificar si la asignación (var1, val1) y (var2, val2) cumple con las restricciones del CSP
    # En este ejemplo, asumimos que todas las restricciones son satisfechas
    return True

# Ejemplo de uso
CSP = {
    'A': [1, 2, 3],
    'B': [1, 2],
    'C': [2, 3]
}

solucion = salto_atras_dirigido_conflictos(CSP)
if solucion is not None:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")
