#Aldo López Barrios
#21310106
#--------------------------

def propagacion_restricciones_colores_mapa(mapa, colores_disponibles):
    # Inicializar la cola de arcos con todos los arcos del mapa
    cola_arcos = [(pais1, pais2) for pais1 in mapa for pais2 in mapa[pais1]]
    
    # Aplicar el algoritmo AC-3 para propagar las restricciones
    while cola_arcos:
        pais1, pais2 = cola_arcos.pop(0)
        if revisar_restriccion(pais1, pais2, colores_disponibles, mapa):
            # Si se realizó alguna revisión en la restricción, agregar los arcos afectados a la cola
            for vecino in mapa[pais1]:
                cola_arcos.append((vecino, pais1))
    
    # Verificar si se encontró una solución al problema
    for pais in mapa:
        if len(mapa[pais]) != 1:
            # Si algún país tiene más de un color asignado, no se encontró solución
            return None
    # Si todas las restricciones se satisfacen, devolver la asignación de colores
    return {pais: colores[0] for pais, colores in mapa.items()}

def revisar_restriccion(pais1, pais2, colores_disponibles, mapa):
    restriccion_actualizada = False
    for color in colores_disponibles:
        # Verificar si el país 1 puede tener el color actual sin conflictos con el país 2
        if color in mapa[pais1] and (pais2 not in mapa[pais1] or len(mapa[pais1]) == 1):
            mapa[pais1] = [color]  # Asignar el color al país 1
            restriccion_actualizada = True
            break
    return restriccion_actualizada

# Ejemplo de uso para resolver el problema de coloración de un mapa de países
mapa = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colores_disponibles = ['Rojo', 'Azul', 'Verde']

solucion = propagacion_restricciones_colores_mapa(mapa, colores_disponibles)
if solucion:
    print("Solución encontrada:")
    for pais, color in solucion.items():
        print(f"Pais {pais} coloreado como {color}")
else:
    print("No se encontró solución.")
