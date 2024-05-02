#Aldo López Barrios
#21310106
#--------------------------

import math

# Definir el símbolo para cada jugador
JUGADOR_X = 'X'
JUGADOR_O = 'O'
VACIO = ' '

# Definir el tamaño del tablero
TAMANO_TABLERO = 3

def imprimir_tablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-' * (TAMANO_TABLERO * 2 - 1))

def tablero_lleno(tablero):
    for fila in tablero:
        if VACIO in fila:
            return False
    return True

def ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(TAMANO_TABLERO):
        if all(tablero[i][j] == jugador for j in range(TAMANO_TABLERO)) or \
           all(tablero[j][i] == jugador for j in range(TAMANO_TABLERO)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(TAMANO_TABLERO)) or \
       all(tablero[i][TAMANO_TABLERO - i - 1] == jugador for i in range(TAMANO_TABLERO)):
        return True

    return False

def minimax(tablero, profundidad, jugador):
    if ganador(tablero, JUGADOR_X):
        return -10 + profundidad
    elif ganador(tablero, JUGADOR_O):
        return 10 - profundidad
    elif tablero_lleno(tablero):
        return 0

    if jugador == JUGADOR_O:
        mejor_valor = -math.inf
        for i in range(TAMANO_TABLERO):
            for j in range(TAMANO_TABLERO):
                if tablero[i][j] == VACIO:
                    tablero[i][j] = JUGADOR_O
                    valor = minimax(tablero, profundidad + 1, JUGADOR_X)
                    tablero[i][j] = VACIO
                    mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = math.inf
        for i in range(TAMANO_TABLERO):
            for j in range(TAMANO_TABLERO):
                if tablero[i][j] == VACIO:
                    tablero[i][j] = JUGADOR_X
                    valor = minimax(tablero, profundidad + 1, JUGADOR_O)
                    tablero[i][j] = VACIO
                    mejor_valor = min(mejor_valor, valor)
        return mejor_valor

def mejor_movimiento(tablero, jugador):
    mejor_valor = -math.inf if jugador == JUGADOR_O else math.inf
    mejor_movimiento = None

    for i in range(TAMANO_TABLERO):
        for j in range(TAMANO_TABLERO):
            if tablero[i][j] == VACIO:
                tablero[i][j] = jugador
                valor = minimax(tablero, 0, JUGADOR_X if jugador == JUGADOR_O else JUGADOR_O)
                tablero[i][j] = VACIO

                if jugador == JUGADOR_O:
                    if valor > mejor_valor:
                        mejor_valor = valor
                        mejor_movimiento = (i, j)
                else:
                    if valor < mejor_valor:
                        mejor_valor = valor
                        mejor_movimiento = (i, j)

    return mejor_movimiento

# Función para jugar al juego de tic-tac-toe
def jugar_tic_tac_toe():
    tablero = [[VACIO] * TAMANO_TABLERO for _ in range(TAMANO_TABLERO)]
    turno = JUGADOR_X

    while not ganador(tablero, JUGADOR_X) and not ganador(tablero, JUGADOR_O) and not tablero_lleno(tablero):
        if turno == JUGADOR_X:
            imprimir_tablero(tablero)
            fila, columna = map(int, input("Jugador X - Ingrese fila y columna separadas por espacio (0-2): ").split())
            if tablero[fila][columna] == VACIO:
                tablero[fila][columna] = JUGADOR_X
                turno = JUGADOR_O
            else:
                print("Casilla ocupada. Intente de nuevo.")
        else:
            fila, columna = mejor_movimiento(tablero, JUGADOR_O)
            tablero[fila][columna] = JUGADOR_O
            turno = JUGADOR_X

    imprimir_tablero(tablero)
    if ganador(tablero, JUGADOR_X):
        print("¡Jugador X gana!")
    elif ganador(tablero, JUGADOR_O):
        print("¡Jugador O gana!")
    else:
        print("¡Empate!")

# Ejecutar el juego
if __name__ == "__main__":
    jugar_tic_tac_toe()
