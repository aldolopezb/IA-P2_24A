#Aldo López Barrios
#21310106
#--------------------------

def backtracking(CSP):
    # Inicializar asignación vacía
    asignacion = {}
    return backtrack_recursivo(CSP, asignacion)

def backtrack_recursivo(CSP, asignacion):
    if es_completa(asignacion, CSP):
        return asignacion
    
    variable_no_asignada = seleccionar_variable_no_asignada(asignacion, CSP)
    for valor in ordenar_valores(variable_no_asignada, CSP):
        if es_consistente(variable_no_asignada, valor, asignacion, CSP):
            asignacion[variable_no_asignada] = valor
            resultado = backtrack_recursivo(CSP, asignacion)
            if resultado:
                return resultado
            del asignacion[variable_no_asignada]
    return None

# Ejemplo de CSP: Mapa de colores
CSP = {
    'WA': ['R', 'G', 'B'],
    'NT': ['R', 'G', 'B'],
    'SA': ['R', 'G', 'B'],
    'Q': ['R', 'G', 'B'],
    'NSW': ['R', 'G', 'B'],
    'V': ['R', 'G', 'B'],
    'T': ['R', 'G', 'B']
}

# Funciones auxiliares
def es_completa(asignacion, CSP):
    return len(asignacion) == len(CSP)

def seleccionar_variable_no_asignada(asignacion, CSP):
    return next(variable for variable in CSP.keys() if variable not in asignacion)

def ordenar_valores(variable, CSP):
    return CSP[variable]

def es_consistente(variable, valor, asignacion, CSP):
    for variable_vecina, valores_vecinos in CSP.items():
        if variable_vecina in asignacion and variable_vecina in vecinos(variable):
            if asignacion[variable_vecina] == valor:
                return False
    return True

def vecinos(variable):
    vecinos = []
    for vecino, valores_vecinos in CSP.items():
        if vecino != variable:
            vecinos.append(vecino)
    return vecinos


# Ejecutar el algoritmo de backtracking
solucion = backtracking(CSP)
if solucion:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró solución.")
