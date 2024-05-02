#Aldo López Barrios
#21310106
#--------------------------

import numpy as np

# Definir los jugadores
JUGADOR_X = 'X'
JUGADOR_O = 'O'
VACIO = ' '

# Definir el tamaño del tablero
FILAS = 6
COLUMNAS = 7

def ganador(tablero, jugador):
    # Verificar filas
    for i in range(FILAS):
        for j in range(COLUMNAS - 3):
            if all(tablero[i][j+k] == jugador for k in range(4)):
                return True

    # Verificar columnas
    for i in range(FILAS - 3):
        for j in range(COLUMNAS):
            if all(tablero[i+k][j] == jugador for k in range(4)):
                return True

    # Verificar diagonales ascendentes
    for i in range(3, FILAS):
        for j in range(COLUMNAS - 3):
            if all(tablero[i-k][j+k] == jugador for k in range(4)):
                return True

    # Verificar diagonales descendentes
    for i in range(FILAS - 3):
        for j in range(COLUMNAS - 3):
            if all(tablero[i+k][j+k] == jugador for k in range(4)):
                return True

    return False

def evaluar(tablero):
    puntaje_x = 0
    puntaje_o = 0

    # Evaluar filas
    for i in range(FILAS):
        for j in range(COLUMNAS - 3):
            fila = tablero[i][j:j+4]
            puntaje_x += fila.count(JUGADOR_X) ** 2
            puntaje_o += fila.count(JUGADOR_O) ** 2

    # Evaluar columnas
    for i in range(FILAS - 3):
        for j in range(COLUMNAS):
            columna = [tablero[i+k][j] for k in range(4)]
            puntaje_x += columna.count(JUGADOR_X) ** 2
            puntaje_o += columna.count(JUGADOR_O) ** 2

    # Evaluar diagonales ascendentes
    for i in range(3, FILAS):
        for j in range(COLUMNAS - 3):
            diagonal = [tablero[i-k][j+k] for k in range(4)]
            puntaje_x += diagonal.count(JUGADOR_X) ** 2
            puntaje_o += diagonal.count(JUGADOR_O) ** 2

    # Evaluar diagonales descendentes
    for i in range(FILAS - 3):
        for j in range(COLUMNAS - 3):
            diagonal = [tablero[i+k][j+k] for k in range(4)]
            puntaje_x += diagonal.count(JUGADOR_X) ** 2
            puntaje_o += diagonal.count(JUGADOR_O) ** 2

    return puntaje_x - puntaje_o

# Crear un tablero de ejemplo
tablero = [
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, JUGADOR_X, VACIO, VACIO, VACIO, VACIO, VACIO],
    [VACIO, JUGADOR_X, JUGADOR_X, JUGADOR_X, JUGADOR_X, VACIO, VACIO],
    [VACIO, VACIO, VACIO, VACIO, VACIO, JUGADOR_O, VACIO],
    [VACIO, VACIO, JUGADOR_X, VACIO, VACIO, JUGADOR_O, VACIO]
]

# Evaluar el tablero
print("Puntaje del tablero:", evaluar(tablero))
