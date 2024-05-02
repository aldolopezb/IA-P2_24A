#Aldo López Barrios
#21310106
#--------------------------

def busqueda_tabu(solucion_inicial, funcion_objetivo, movimientos_tabu, max_iter):
    mejor_solucion = solucion_inicial
    mejor_valor = funcion_objetivo(solucion_inicial)
    solucion_actual = solucion_inicial
    iteracion = 0
    lista_tabu = []

    while iteracion < max_iter:
        vecinos = generar_vecinos(solucion_actual)
        
        # Verificar si la lista de vecinos está vacía
        if not vecinos:
            break
        
        mejor_vecino = min(vecinos, key=funcion_objetivo)
        
        if mejor_valor > funcion_objetivo(mejor_vecino) and mejor_vecino not in lista_tabu:
            mejor_solucion = mejor_vecino
            mejor_valor = funcion_objetivo(mejor_vecino)
        
        solucion_actual = mejor_vecino
        lista_tabu.append(solucion_actual)
        if len(lista_tabu) > movimientos_tabu:
            lista_tabu.pop(0)

        iteracion += 1

    return mejor_solucion

# Función de ejemplo para generar vecinos (Debes completar esta función según tu problema específico)
def generar_vecinos(solucion_actual):
    vecinos = []
    # Implementa la lógica para generar vecinos aquí
    return vecinos

# Función de ejemplo para evaluar una solución (Debes completar esta función según tu problema específico)
def funcion_objetivo(solucion):
    # Implementa la lógica para evaluar la solución aquí
    pass

# Ejemplo de uso
# Define la solución inicial y otros parámetros según tu problema específico
solucion_inicial = ...  
solucion_final = busqueda_tabu(solucion_inicial, funcion_objetivo, movimientos_tabu=10, max_iter=100)
print("Mejor solución encontrada:", solucion_final)
