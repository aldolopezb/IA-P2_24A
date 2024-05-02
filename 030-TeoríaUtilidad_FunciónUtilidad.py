#Aldo López Barrios
#21310106
#--------------------------

def calcular_utilidad(jugador, estado):
    """
    Calcula la utilidad del estado actual para un jugador dado.
    """
    if estado == "Victoria":
        if jugador == "Max":
            return 1  # Jugador "Max" gana
        else:
            return -1  # Jugador "Min" pierde
    elif estado == "Derrota":
        if jugador == "Max":
            return -1  # Jugador "Max" pierde
        else:
            return 1  # Jugador "Min" gana
    else:
        return 0  # Empate o juego en curso

# Ejemplo de uso
estado_actual = "Victoria"  # Estado actual del juego
jugador_actual = "Max"  # Jugador actual
utilidad = calcular_utilidad(jugador_actual, estado_actual)
print("Utilidad para el jugador actual:", utilidad)
