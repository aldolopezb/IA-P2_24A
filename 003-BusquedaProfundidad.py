#Aldo López Barrios
#21310106
#--------------------------
#Recorrer o buscar en estructuras de datos de árboles o grafos

# Definimos la función de búsqueda en profundidad
def dfs(graph, start):
    # Creamos un conjunto para almacenar los nodos visitados
    visited = set()
    # Creamos una pila e inicializamos con el nodo de inicio
    stack = [start]

    while stack:
        # Tomamos el último nodo de la pila
        node = stack.pop()
        # Si el nodo no ha sido visitado
        if node not in visited:
            # Lo marcamos como visitado
            visited.add(node)
            # Agregamos los vecinos del nodo a la pila
            stack.extend(graph[node] - visited)
    return visited

# Definimos un grafo como un diccionario
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print(dfs(graph, 'A'))  # Imprime todos los nodos visitados
