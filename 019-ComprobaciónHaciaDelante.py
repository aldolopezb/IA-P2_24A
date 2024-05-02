#Aldo López Barrios
#21310106
#--------------------------

def forward_checking_coloracion_grafo(grafo, colores_disponibles):
    # Función principal que llama al algoritmo de comprobación hacia adelante para resolver el problema de coloración de un grafo
    return forward_checking_recursivo_coloracion_grafo({}, grafo, colores_disponibles)

def forward_checking_recursivo_coloracion_grafo(asignacion, grafo, colores_disponibles):
    # Función recursiva que realiza la comprobación hacia adelante y busca una solución al problema de coloración de un grafo
    
    # Verificar si se ha completado la asignación de colores a todos los nodos
    if len(asignacion) == len(grafo):
        return asignacion
    
    # Obtener el próximo nodo a colorear
    nodo_actual = obtener_nodo_sin_color(asignacion, grafo)
    
    # Iterar sobre los colores disponibles para el nodo actual
    for color in colores_disponibles:
        # Verificar si el color actual es válido para el nodo actual y sus vecinos
        if es_color_valido(nodo_actual, color, asignacion, grafo):
            # Si el color es válido, asignarlo al nodo actual
            asignacion[nodo_actual] = color
            
            # Llamar recursivamente a la función para continuar con el siguiente nodo
            resultado = forward_checking_recursivo_coloracion_grafo(asignacion, grafo, colores_disponibles)
            
            # Si se encuentra una solución, devolverla
            if resultado:
                return resultado
            
            # Si no se encuentra una solución, retroceder y eliminar el color asignado al nodo actual
            del asignacion[nodo_actual]
    
    # Si no se encontró ninguna solución para el nodo actual, devolver None
    return None

def obtener_nodo_sin_color(asignacion, grafo):
    # Función para obtener un nodo del grafo que aún no ha sido coloreado
    for nodo in grafo:
        if nodo not in asignacion:
            return nodo
    return None

def es_color_valido(nodo, color, asignacion, grafo):
    # Función para verificar si un color es válido para un nodo y sus vecinos en el grafo
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Ejemplo de uso para resolver el problema de coloración de un grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colores_disponibles = ['Rojo', 'Azul', 'Verde']

solucion = forward_checking_coloracion_grafo(grafo, colores_disponibles)
if solucion:
    print("Solución encontrada:")
    for nodo, color in solucion.items():
        print(f"Nodo {nodo} coloreado como {color}")
else:
    print("No se encontró solución.")
