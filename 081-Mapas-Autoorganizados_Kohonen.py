#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
import matplotlib.pyplot as plt

class KohonenMap:
    def __init__(self, input_size, map_size):
        self.input_size = input_size
        self.map_size = map_size
        self.weights = np.random.rand(map_size[0], map_size[1], input_size)

    def find_best_matching_unit(self, input_vector):
        distances = np.linalg.norm(self.weights - input_vector, axis=2)
        indices = np.unravel_index(np.argmin(distances), distances.shape)
        return indices

    def update_weights(self, input_vector, bmu_indices, learning_rate, radius):
        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                distance = np.linalg.norm(np.array([i, j]) - np.array(bmu_indices))
                if distance <= radius:
                    self.weights[i, j] += learning_rate * (input_vector - self.weights[i, j])

    def train(self, data, num_epochs, initial_learning_rate, initial_radius):
        for epoch in range(1, num_epochs + 1):
            learning_rate = initial_learning_rate * (1 - epoch / num_epochs)
            radius = initial_radius * (1 - epoch / num_epochs)
            for input_vector in data:
                bmu_indices = self.find_best_matching_unit(input_vector)
                self.update_weights(input_vector, bmu_indices, learning_rate, radius)
            print(f"Epoch {epoch}/{num_epochs}")

    def visualize(self):
        plt.imshow(self.weights)
        plt.title('Kohonen Map')
        plt.colorbar()
        plt.show()

# Datos de ejemplo (4 ejemplos de 3 características)
data = np.array([[0.1, 0.2, 0.3],
                 [0.4, 0.5, 0.6],
                 [0.7, 0.8, 0.9],
                 [0.2, 0.7, 0.5]])

# Crear e inicializar el mapa autoorganizado de Kohonen
input_size = len(data[0])
map_size = (5, 5)  # Tamaño del mapa (5x5)
kohonen_map = KohonenMap(input_size, map_size)

# Entrenar el mapa
kohonen_map.train(data, num_epochs=1000, initial_learning_rate=0.1, initial_radius=2.5)

# Visualizar el mapa
kohonen_map.visualize()
