class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Función para verificar si se puede colorear un vértice con un color dado
    def es_seguro(self, v, color, c):
        for i in range(self.V):
            if self.grafo[v][i] == 1 and color[i] == c:
                return False
        return True

    # Función utilitaria recursiva para colorear el grafo
    def colorear_grafo_util(self, m, color, v):
        # Si todos los vértices están coloreados, hemos terminado
        if v == self.V:
            return True
        # Probar diferentes colores para el vértice v
        for c in range(1, m+1):
            # Si es seguro asignar el color c al vértice v
            if self.es_seguro(v, color, c):
                color[v] = c
                # Probar recursivamente para los vértices restantes
                if self.colorear_grafo_util(m, color, v+1):
                    return True
                # Si la asignación no lleva a una solución, volver atrás y probar otro color
                color[v] = 0

    # Función principal para colorear el grafo
    def colorear_grafo(self, m):
        color = [0] * self.V  # Inicializar la lista de colores con 0
        # Llamar a la función utilitaria para colorear el grafo
        if not self.colorear_grafo_util(m, color, 0):
            print("No es posible colorear el grafo con", m, "colores.")
            return False
        # Si se encuentra una solución, imprimir la asignación de colores
        print("Asignación de colores:")
        for c in color:
            print(c, end=" ")
        return True


# Ejemplo de uso
g = Grafo(4)  # Crear un grafo con 4 vértices
g.grafo = [[0, 1, 1, 1],   # Definir la matriz de adyacencia del grafo
           [1, 0, 1, 0],
           [1, 1, 0, 1],
           [1, 0, 1, 0]]

m = 3  # Número de colores disponibles
g.colorear_grafo(m)  # Resolver y colorear el grafo con m colores
