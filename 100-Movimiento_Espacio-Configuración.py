#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
import matplotlib.pyplot as plt

# Clase para el nodo del árbol RRT
class Node:
    def __init__(self, position):
        self.position = position
        self.parent = None

# Función para generar un punto aleatorio dentro del espacio de configuración
def generate_random_point(x_lim, y_lim):
    x = np.random.uniform(x_lim[0], x_lim[1])
    y = np.random.uniform(y_lim[0], y_lim[1])
    return [x, y]

# Función para encontrar el nodo más cercano en el árbol RRT
def find_nearest_node(tree, point):
    distances = [np.linalg.norm(node.position - point) for node in tree]
    nearest_node_index = np.argmin(distances)
    return tree[nearest_node_index]

# Función para expandir el árbol RRT hacia un punto aleatorio
def expand_tree(tree, nearest_node, random_point, step_size):
    direction = random_point - nearest_node.position
    direction /= np.linalg.norm(direction)
    new_point = nearest_node.position + direction * step_size
    new_node = Node(new_point)
    new_node.parent = nearest_node
    return new_node

# Función para planificar una ruta utilizando el algoritmo RRT
def rrt(start, goal, x_lim, y_lim, max_iterations=1000, step_size=0.1):
    # Inicializar el árbol RRT con el nodo inicial
    tree = [Node(np.array(start))]
    
    for _ in range(max_iterations):
        # Generar un punto aleatorio
        random_point = np.array(generate_random_point(x_lim, y_lim))
        
        # Encontrar el nodo más cercano en el árbol RRT
        nearest_node = find_nearest_node(tree, random_point)
        
        # Expandir el árbol hacia el punto aleatorio
        new_node = expand_tree(tree, nearest_node, random_point, step_size)
        
        # Si el nuevo nodo está dentro de una distancia pequeña del objetivo, terminar la búsqueda
        if np.linalg.norm(new_node.position - np.array(goal)) < step_size:
            new_node.parent = nearest_node
            tree.append(new_node)
            return tree
        
        # Agregar el nuevo nodo al árbol RRT
        tree.append(new_node)
    
    return None

# Función para trazar la ruta encontrada por el algoritmo RRT
def plot_rrt(start, goal, tree):
    plt.figure(figsize=(8, 6))
    plt.plot(start[0], start[1], 'go', markersize=10, label='Start')
    plt.plot(goal[0], goal[1], 'ro', markersize=10, label='Goal')
    if tree is not None:
        for node in tree:
            if node.parent:
                plt.plot([node.position[0], node.parent.position[0]], [node.position[1], node.parent.position[1]], 'b-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Rapidly-exploring Random Tree (RRT)')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Definir el punto de inicio y el objetivo
start = [0, 0]
goal = [5, 5]

# Definir los límites del espacio de configuración
x_lim = [-1, 6]
y_lim = [-1, 6]

# Ejecutar el algoritmo RRT para planificar la ruta
tree = rrt(start, goal, x_lim, y_lim)

# Visualizar la ruta encontrada por el algoritmo RRT
plot_rrt(start, goal, tree)
