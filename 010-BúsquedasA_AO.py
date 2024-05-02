#Aldo López Barrios
#21310106
#--------------------------

import heapq

def distancia_euclidiana(nodo, objetivo):
    # Función heurística (distancia euclidiana)
    x1, y1 = nodo
    x2, y2 = objetivo
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def astar(grafo, inicio, objetivo):
    cola = [(0, inicio)]  # Inicializamos la cola de prioridad con el nodo inicial
    visitados = set()     # Conjunto de nodos visitados
    while cola:
        costo, nodo_actual = heapq.heappop(cola)  # Sacamos el nodo con menor costo de la cola
        if nodo_actual == objetivo:
            return True  # Si el nodo actual es el objetivo, devolvemos verdadero
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)  # Marcamos el nodo como visitado
            for vecino, peso in grafo[nodo_actual]:
                # Agregamos los vecinos del nodo actual a la cola con su costo y heurística
                heapq.heappush(cola, (costo + peso + distancia_euclidiana(vecino, objetivo), vecino))
    return False  # Si no se encuentra el objetivo, devolvemos falso

# Ejemplo de grafo representado como lista de adyacencia con pesos
grafo = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((0, 1), 1), ((1, 0), 1)]
}

inicio_nodo = (0, 0)
objetivo_nodo = (1, 1)
print("¿Se encontró el objetivo?:", astar(grafo, inicio_nodo, objetivo_nodo))
