#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

# Definir el entorno (matriz 2D)
grid = np.array([
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
])

# Definir la distribución inicial de creencias (uniforme)
beliefs = np.ones(grid.shape) / np.prod(grid.shape)

# Función para imprimir la distribución de creencias
def print_beliefs(beliefs):
    for row in beliefs:
        print(' '.join([f'{prob:.2f}' for prob in row]))

# Definir la función de movimiento (desplazamiento de 1 casilla)
def move(x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dx, dy = np.random.choice([-1, 0, 1]), np.random.choice([-1, 0, 1])
    new_x, new_y = x + dx, y + dy
    return max(0, min(new_x, grid.shape[0] - 1)), max(0, min(new_y, grid.shape[1] - 1))

# Definir la función de observación
def sense(x, y):
    return grid[x, y] == 1

# Inicializar las coordenadas del agente
x, y = 0, 0

# Número de iteraciones de Monte Carlo
num_iterations = 1000

# Realizar la localización por Monte Carlo
for _ in range(num_iterations):
    # Movimiento del agente
    x, y = move(x, y)

    # Observación
    if sense(x, y):
        beliefs[x, y] *= 0.9  # Probabilidad de observar un obstáculo
    else:
        beliefs[x, y] *= 0.1  # Probabilidad de no observar un obstáculo

    # Normalizar las creencias
    beliefs /= np.sum(beliefs)

# Imprimir la distribución final de creencias
print("Distribución final de creencias:")
print_beliefs(beliefs)
