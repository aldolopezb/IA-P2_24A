#Aldo López Barrios
#21310106
#--------------------------

import numpy as np

def encontrar_equilibrio_nash(pagos_jugador1, pagos_jugador2):
    num_estrategias_jugador1 = len(pagos_jugador1)
    num_estrategias_jugador2 = len(pagos_jugador2)

    # Encontrar el índice del máximo pago para el jugador 1 en cada estrategia del jugador 2
    mejores_estrategias_jugador1 = [np.argmax(pagos_jugador1[:, j]) for j in range(num_estrategias_jugador2)]

    # Encontrar el índice del máximo pago para el jugador 2 en cada estrategia del jugador 1
    mejores_estrategias_jugador2 = [np.argmax(pagos_jugador2[i, :]) for i in range(num_estrategias_jugador1)]

    # Verificar si existe un equilibrio de Nash
    equilibrio_nash = []
    for i in range(num_estrategias_jugador1):
        for j in range(num_estrategias_jugador2):
            if mejores_estrategias_jugador1[j] == i and mejores_estrategias_jugador2[i] == j:
                equilibrio_nash.append((i, j))

    return equilibrio_nash

# Ejemplo de uso
pagos_jugador1 = np.array([[3, 2],
                            [1, 4]])

pagos_jugador2 = np.array([[3, 1],
                            [2, 4]])

equilibrio_nash = encontrar_equilibrio_nash(pagos_jugador1, pagos_jugador2)
if equilibrio_nash:
    print("Equilibrio de Nash encontrado en las siguientes estrategias:")
    for estrategia_jugador1, estrategia_jugador2 in equilibrio_nash:
        print(f"Estrategia Jugador 1: {estrategia_jugador1 + 1}, Estrategia Jugador 2: {estrategia_jugador2 + 1}")
else:
    print("No se encontró ningún equilibrio de Nash en el juego.")
