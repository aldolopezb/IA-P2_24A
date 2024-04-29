#Aldo López Barrios
#21310106
#--------------------------

from collections import deque

def bfs(graph, root, goal):
    visitados = set()  # Conjunto para almacenar los nodos visitados
    queue = deque([(root, [root])])  # Cola para los nodos a visitar, almacenamos el nodo y el camino hasta él

    while queue:
        (node, path) = queue.popleft()  # Obtenemos el nodo y el camino hasta él
        if node not in visitados:
            if node == goal:  # Si el nodo es el objetivo, retornamos el camino hasta él
                return path
            visitados.add(node)  # Marcamos el nodo como visitado
            for vecinos in graph[node]:  # Agregamos a la cola todos los vecinos del nodo
                queue.append((vecinos, path + [vecinos]))

    return None  # Si no hay camino hasta el objetivo, retornamos None

# Definimos un grafo como un diccionario
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs(graph, 'A', 'F'))  # Imprime: ['A', 'C', 'F']

#Se prueba la función con un grafo de ejemplo y se imprime el camino más corto desde el nodo ‘A’ hasta el nodo ‘F’.