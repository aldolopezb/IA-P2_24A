#Aldo López Barrios
#21310106
#--------------------------

def ascenso_colinas(grafo, inicio):
    nodo_actual = inicio
    while True:
        vecinos = grafo[nodo_actual]
        mejor_vecino = max(vecinos, key=lambda x: grafo[x])  # Selecciona el vecino con el mayor valor (ascenso de colinas)
        if grafo[mejor_vecino] <= grafo[nodo_actual]:
            return nodo_actual  # Si no hay un vecino mejor, devuelve el nodo actual
        nodo_actual = mejor_vecino

# Ejemplo de grafo representado como diccionario de nodos y sus valores asociados
grafo = {
    (0, 0): 10,
    (0, 1): 8,
    (1, 0): 12,
    (1, 1): 5,
    (2, 2): 6
}

inicio_nodo = (0, 0)
print("Máximo local encontrado:", inicio_nodo)
