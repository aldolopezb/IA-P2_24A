#Aldo López Barrios
#21310106
#--------------------------

def busqueda_bidireccional(grafo, inicio, objetivo):
    cola_adelante = [inicio]  # Cola para la búsqueda desde el inicio
    cola_atras = [objetivo]  # Cola para la búsqueda desde el objetivo
    visitados_adelante = {inicio}  # Conjunto de nodos visitados en la búsqueda desde el inicio
    visitados_atras = {objetivo}  # Conjunto de nodos visitados en la búsqueda desde el objetivo
    
    while cola_adelante and cola_atras:
        # Expandir búsqueda desde el inicio
        actual_adelante = cola_adelante.pop(0)
        for vecino in grafo[actual_adelante]:
            if vecino in visitados_atras:
                return True  # Ruta encontrada
            if vecino not in visitados_adelante:
                visitados_adelante.add(vecino)
                cola_adelante.append(vecino)
        
        # Expandir búsqueda desde el objetivo
        actual_atras = cola_atras.pop(0)
        for vecino in grafo[actual_atras]:
            if vecino in visitados_adelante:
                return True  # Ruta encontrada
            if vecino not in visitados_atras:
                visitados_atras.add(vecino)
                cola_atras.append(vecino)
    
    return False  # No se encontró ruta

# Ejemplo de grafo representado como lista de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

nodo_inicio = 'A'
nodo_objetivo = 'F'
print("Ruta encontrada:", busqueda_bidireccional(grafo, nodo_inicio, nodo_objetivo))

