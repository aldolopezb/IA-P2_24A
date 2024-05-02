#Aldo López Barrios
#21310106
#--------------------------

import heapq

def distancia_euclidiana(nodo, objetivo):
    # Función heurística (distancia euclidiana)
    x1, y1 = nodo
    x2, y2 = objetivo
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def busqueda_voraz(grafo, inicio, objetivo):
    cola = [(distancia_euclidiana(inicio, objetivo), inicio)]  # Inicializamos la cola de prioridad con la distancia al objetivo
    visitados = set()  # Conjunto de nodos visitados
    while cola:
        _, nodo_actual = heapq.heappop(cola)  # Sacamos el nodo con menor distancia al objetivo de la cola
        if nodo_actual == objetivo:
            return True  # Si el nodo actual es el objetivo, devolvemos verdadero
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)  # Marcamos el nodo como visitado
            for vecino in grafo[nodo_actual]:
                heapq.heappush(cola, (distancia_euclidiana(vecino, objetivo), vecino))  # Agregamos los vecinos a la cola con su distancia al objetivo
    return False  # Si no se encuentra el objetivo, devolvemos falso

# Ejemplo de grafo representado como lista de adyacencia
grafo = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (1, 0)]
}

inicio_nodo = (0, 0)
objetivo_nodo = (1, 1)
print("¿Se encontró el objetivo?:", busqueda_voraz(grafo, inicio_nodo, objetivo_nodo))
