#Aldo López Barrios
#21310106
#--------------------------

def dfs(grafo, inicio, objetivo, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    if inicio == objetivo:
        return True  # Si el nodo actual es el objetivo, devolvemos verdadero
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            if dfs(grafo, vecino, objetivo, visitados):
                return True  # Si encontramos el objetivo en el vecino, devolvemos verdadero
    return False  # Si no se encuentra el objetivo en los vecinos, devolvemos falso

# Ejemplo de grafo representado como lista de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

inicio_nodo = 'A'
objetivo_nodo = 'F'
print("Camino encontrado:", dfs(grafo, inicio_nodo, objetivo_nodo))
