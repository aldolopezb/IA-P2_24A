#Aldo López Barrios
#21310106
#--------------------------

# Definimos la función de búsqueda en profundidad limitada
def dls(graph, start, limit):
    visited = set()
    stack = [(start, 0)]

    while stack:
        node, depth = stack.pop()
        if node not in visited:
            visited.add(node)
            if depth < limit:
                stack.extend((neighbor, depth + 1) for neighbor in graph[node] - visited)
    return visited

# Definimos la función de búsqueda en profundidad iterativa
def ids(graph, start, max_depth):
    for limit in range(max_depth + 1):
        visited = dls(graph, start, limit)
        if visited:
            return visited
    return None

# Definimos un grafo como un diccionario
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


print(ids(graph, 'A', 3))  # Imprime: {'A', 'B', 'C', 'D', 'E'}
