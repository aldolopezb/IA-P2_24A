#Aldo López Barrios
#21310106
#--------------------------

import heapq

def dist_heuristica(nodo, objetivo):
    # Función heurística (distancia de Manhattan)
    x1, y1 = nodo
    x2, y2 = objetivo
    return abs(x2 - x1) + abs(y2 - y1)

def astar(grafo, inicio, objetivo):
    cola = [(0, inicio)]  # Inicializamos la cola de prioridad con el nodo inicial
    visitados = set()     # Conjunto de nodos visitados
    while cola:
        costo, nodo_actual = heapq.heappop(cola)  # Sacamos el nodo con menor costo de la cola
        if nodo_actual == objetivo:
            return costo  # Si el nodo actual es el objetivo, devolvemos el costo acumulado
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)  # Marcamos el nodo como visitado
            for vecino, peso in grafo[nodo_actual]:
                # Agregamos los vecinos del nodo actual a la cola con su costo y heurística
                nuevo_costo = costo + peso
                heapq.heappush(cola, (nuevo_costo + dist_heuristica(vecino, objetivo), vecino))
    return float('inf')  # Si no se encuentra una ruta al objetivo, devolvemos infinito

# Ejemplo de grafo representado como lista de adyacencia con pesos
grafo = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((0, 1), 1), ((1, 0), 1)]
}

inicio_nodo = (0, 0)
objetivo_nodo = (1, 1)
print("Costo del camino más corto:", astar(grafo, inicio_nodo, objetivo_nodo))

