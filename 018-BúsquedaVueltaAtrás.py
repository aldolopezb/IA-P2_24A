#Aldo López Barrios
#21310106
#--------------------------

def es_completa(asignacion, n):
    return len(asignacion) == n

def es_consistente(asignacion, fila, columna):
    for fila_anterior, columna_anterior in asignacion.items():
        if columna_anterior == columna or abs(fila_anterior - fila) == abs(columna_anterior - columna):
            return False
    return True

def backtracking_n_reinas(n):
    asignacion = {}
    if backtrack_recursivo_n_reinas(asignacion, 0, n):
        return asignacion
    else:
        return None

def backtrack_recursivo_n_reinas(asignacion, fila, n):
    if es_completa(asignacion, n):
        return True
    
    for columna in range(n):
        if es_consistente(asignacion, fila, columna):
            asignacion[fila] = columna
            if backtrack_recursivo_n_reinas(asignacion, fila + 1, n):
                return True
            del asignacion[fila]
    
    return False

# Ejemplo de uso para resolver el problema de las 8 reinas
n = 8
solucion = backtracking_n_reinas(n)
if solucion:
    print("Solución encontrada:")
    for fila, columna in solucion.items():
        print(f"Reina en fila {fila+1}, columna {columna+1}")
else:
    print("No se encontró solución.")



'''

Q - - - - - - -
- - - - Q - - -
- - - - - - - Q
- - - - - Q - -
- - Q - - - - -
- - - - - - Q -
- Q - - - - - -
- - - Q - - - -

'''