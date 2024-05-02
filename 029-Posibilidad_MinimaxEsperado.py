#Aldo López Barrios
#21310106
#--------------------------

import random

def evaluar_estado(estado):
    """
    Función de evaluación simple para el juego.
    """
    if estado == "Ganador":
        return 1
    elif estado == "Perdedor":
        return -1
    else:
        return 0

def minimax_esperado(estado, profundidad, jugador):
    """
    Implementación del algoritmo Minimax Esperado.
    """
    if profundidad == 0 or estado.finalizado():
        return evaluar_estado(estado)

    if jugador == "Max":
        valor_max = float('-inf')
        for movimiento in estado.movimientos():
            nuevo_estado = estado.simular_movimiento(movimiento)
            valor = minimax_esperado(nuevo_estado, profundidad - 1, "Min")
            valor_max = max(valor_max, valor)
        return valor_max
    else:
        valor_min = float('inf')
        for movimiento in estado.movimientos():
            nuevo_estado = estado.simular_movimiento(movimiento)
            valor = minimax_esperado(nuevo_estado, profundidad - 1, "Max")
            valor_min = min(valor_min, valor)
        return valor_min

def minimax_esperado_probabilidad(estado, profundidad, jugador):
    """
    Implementación del algoritmo Minimax Esperado con probabilidad.
    """
    if profundidad == 0 or estado.finalizado():
        return evaluar_estado(estado)

    if jugador == "Max":
        valor_max = float('-inf')
        for movimiento in estado.movimientos():
            nuevo_estado = estado.simular_movimiento(movimiento)
            valor = minimax_esperado_probabilidad(nuevo_estado, profundidad - 1, "Min")
            valor_max = max(valor_max, valor)
        return valor_max
    else:
        valor_min = float('inf')
        for movimiento in estado.movimientos():
            nuevo_estado = estado.simular_movimiento(movimiento)
            valor = minimax_esperado_probabilidad(nuevo_estado, profundidad - 1, "Max")
            valor_min = min(valor_min, valor)
        return valor_min

# Clase para representar el estado del juego
class EstadoJuego:
    def __init__(self):
        self.estado_actual = "En curso"

    def finalizado(self):
        return self.estado_actual != "En curso"

    def movimientos(self):
        return [1, 2, 3]  # Ejemplo de movimientos posibles

    def simular_movimiento(self, movimiento):
        # Simular el movimiento y devolver un nuevo estado
        return EstadoJuego()  # Se debe implementar según las reglas del juego

# Crear un estado inicial del juego
estado_inicial = EstadoJuego()

# Ejecutar el algoritmo Minimax Esperado
profundidad_max = 3
valor = minimax_esperado(estado_inicial, profundidad_max, "Max")
print("Valor de la posición con Minimax Esperado:", valor)

# Ejecutar el algoritmo Minimax Esperado con probabilidad
valor_probabilidad = minimax_esperado_probabilidad(estado_inicial, profundidad_max, "Max")
print("Valor de la posición con Minimax Esperado con probabilidad:", valor_probabilidad)
