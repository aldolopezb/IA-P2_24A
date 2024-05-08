#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

class HopfieldNetwork:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))

    def train(self, patterns):
        num_patterns = len(patterns)
        for pattern in patterns:
            pattern_matrix = np.outer(pattern, pattern)
            np.fill_diagonal(pattern_matrix, 0)
            self.weights += pattern_matrix
        self.weights /= num_patterns

    def energy(self, state):
        return -0.5 * np.dot(state.T, np.dot(self.weights, state))

    def update(self, state, max_iters=100):
        for _ in range(max_iters):
            new_state = np.sign(np.dot(self.weights, state))
            if np.array_equal(new_state, state):
                break
            state = new_state
        return state

# Ejemplo de patrones
pattern1 = np.array([1, 1, 1, 1, 1])
pattern2 = np.array([-1, -1, -1, -1, -1])
pattern3 = np.array([1, -1, 1, -1, 1])

# Crear la red Hopfield y entrenarla con los patrones
hopfield_net = HopfieldNetwork(len(pattern1))
hopfield_net.train([pattern1, pattern2, pattern3])

# Estado inicial
initial_state = np.array([1, 1, 1, -1, 1])

# Actualizar el estado de la red
final_state = hopfield_net.update(initial_state)

print("Estado inicial:", initial_state)
print("Estado final:", final_state)
print("Energía final:", hopfield_net.energy(final_state))
