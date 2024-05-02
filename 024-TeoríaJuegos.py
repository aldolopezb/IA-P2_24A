#Aldo López Barrios
#21310106
#--------------------------

import nashpy as nash

# Definir las matrices de pagos para los dos jugadores
matriz_pagos_jugador1 = [[3, 0], [5, 1]]
matriz_pagos_jugador2 = [[3, 5], [0, 1]]

# Crear los objetos de juego para cada jugador
juego_jugador1 = nash.Game(matriz_pagos_jugador1)
juego_jugador2 = nash.Game(matriz_pagos_jugador2)

# Calcular los equilibrios de Nash y convertir el generador en una lista
equilibrio_nash = list(juego_jugador1.support_enumeration())

# Verificar si se encontraron equilibrios de Nash
if equilibrio_nash:
    # Obtener el primer equilibrio de Nash
    primer_equilibrio = equilibrio_nash[0]
    
    # Calcular el pago esperado para cada jugador en el equilibrio de Nash
    pago_jugador1, pago_jugador2 = juego_jugador1[primer_equilibrio], juego_jugador2[primer_equilibrio]
    print("Pago esperado para el jugador 1:", pago_jugador1)
    print("Pago esperado para el jugador 2:", pago_jugador2)
else:
    print("No se encontraron equilibrios de Nash.")
