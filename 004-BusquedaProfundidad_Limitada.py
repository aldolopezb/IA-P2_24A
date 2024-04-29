#Aldo López Barrios
#21310106
#--------------------------

# Definimos la función de búsqueda en profundidad limitada
def dls(graph, start, limit):
    # Creamos un conjunto para almacenar los nodos visitados
    visited = set()
    # Creamos una pila e inicializamos con el nodo de inicio y la profundidad 0
    stack = [(start, 0)]

    while stack:
        # Tomamos el último nodo de la pila y su profundidad
        node, depth = stack.pop()
        # Si el nodo no ha sido visitado
        if node not in visited:
            # Lo marcamos como visitado
            visited.add(node)
            # Si no hemos alcanzado el límite de profundidad
            if depth < limit:
                # Agregamos los vecinos del nodo a la pila con profundidad incrementada
                stack.extend((neighbor, depth + 1) for neighbor in graph[node])
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

print(dls(graph, 'A', 2))  # Se imprimen todos los nodos visitados hasta una profundidad de 2.
