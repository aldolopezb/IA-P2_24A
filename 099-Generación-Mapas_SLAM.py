#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
import matplotlib.pyplot as plt

# Definir la clase del robot
class Robot:
    def __init__(self, initial_pose):
        self.pose = initial_pose

    def move(self, delta_x, delta_y):
        self.pose[0] += delta_x
        self.pose[1] += delta_y

# Función para visualizar el mapa y la posición del robot
def plot_map(robot, landmarks):
    plt.figure(figsize=(8, 6))
    # Dibujar el mapa
    for landmark in landmarks:
        plt.plot(landmark[0], landmark[1], 'ko', markersize=10)
    # Dibujar la posición actual del robot
    plt.plot(robot.pose[0], robot.pose[1], 'r^', markersize=10)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('SLAM: Simultaneous Localization and Mapping')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Definir las landmarks (puntos de referencia)
landmarks = [[2, 2], [6, 2], [4, 6], [8, 6]]

# Crear el robot en una posición inicial conocida
initial_pose = [0, 0]
robot = Robot(initial_pose)

# Realizar movimientos del robot y actualizar el mapa
for _ in range(5):
    # Movimiento del robot (simulado)
    delta_x, delta_y = np.random.normal(0.1, 0.05), np.random.normal(0.1, 0.05)
    robot.move(delta_x, delta_y)
    
    # Visualizar el mapa y la posición del robot después de cada movimiento
    plot_map(robot, landmarks)
