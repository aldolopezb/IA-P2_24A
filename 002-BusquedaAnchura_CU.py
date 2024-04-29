#Aldo López Barrios
#21310106
#--------------------------
#Encontrar el costo acumulativo mínimo de la ruta desde un nodo fuente hasta un nodo destino

# Importamos la biblioteca PriorityQueue de Python
from queue import PriorityQueue

def BusquedaCostoUniforme(graph, start, goal):
    # Creamos un conjunto para almacenar los nodos visitados
    visited = set()
    # Creamos una cola de prioridad para los nodos a visitar
    queue = PriorityQueue()
    # Agregamos el nodo inicial a la cola con costo 0 y sin camino
    queue.put((0, start, []))

    # Mientras la cola no esté vacía
    while not queue.empty():
        # Obtenemos el nodo con el costo mínimo y el camino hasta él
        cost, node, path = queue.get()
        # Si el nodo no ha sido visitado
        if node not in visited:
            # Agregamos el nodo al camino
            path = path + [node]
            # Si el nodo es el objetivo
            if node == goal:
                # Retornamos el costo y el camino hasta el nodo
                return cost, path
            # Agregamos el nodo a los nodos visitados
            visited.add(node)
            # Para cada vecino del nodo
            for neighbor, neighbor_cost in graph[node].items():
                # Si el vecino no ha sido visitado
                if neighbor not in visited:
                    # Calculamos el costo total hasta el vecino
                    total_cost = cost + neighbor_cost
                    # Agregamos el vecino a la cola con su costo y camino
                    queue.put((total_cost, neighbor, path))
    # Si no hay camino hasta el objetivo, retornamos None
    return None

# Definimos un grafo como un diccionario
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 3, 'E': 4},
    'C': {'A': 5, 'F': 1},
    'D': {'B': 3},
    'E': {'B': 4, 'F': 7},
    'F': {'C': 1, 'E': 7}
}

# Llamamos a la función con el grafo y los nodos de inicio y fin
cost, path = BusquedaCostoUniforme(graph, 'A', 'F')
# Imprimimos el costo y el camino
print(f"Cost: {cost}, Path: {path}")  # Debería imprimir: Cost: 6, Path: ['A', 'B', 'D', 'E', 'F']
