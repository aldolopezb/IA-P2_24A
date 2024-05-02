#Aldo López Barrios
#21310106
#--------------------------

from collections import deque

def busqueda_en_linea(estado_inicial, es_estado_objetivo, generar_sucesores):
    frontera = deque([estado_inicial])

    while frontera:
        estado_actual = frontera.popleft()
        if es_estado_objetivo(estado_actual):
            return estado_actual
        
        sucesores = generar_sucesores(estado_actual)
        frontera.extend(sucesores)

    return None  # No se encontró el estado objetivo

# Ejemplo de uso
# Definir funciones auxiliares para el problema específico
def es_estado_objetivo(estado):
    return estado == "G"

def generar_sucesores(estado):
    sucesores = []
    if estado != "A":
        sucesores.append(chr(ord(estado) - 1))
    if estado != "Z":
        sucesores.append(chr(ord(estado) + 1))
    return sucesores

# Ejecutar la búsqueda en línea
estado_inicial = "A"
estado_objetivo = busqueda_en_linea(estado_inicial, es_estado_objetivo, generar_sucesores)
if estado_objetivo:
    print("Se encontró el estado objetivo:", estado_objetivo)
else:
    print("No se encontró el estado objetivo.")
