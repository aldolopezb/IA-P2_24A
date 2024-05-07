#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

class MarkovChain:
    def __init__(self, transition_matrix, states):
        self.transition_matrix = np.array(transition_matrix)
        self.states = states
        self.current_state = np.random.choice(states)

    def next_state(self):
        idx = np.where(self.states == self.current_state)[0][0]
        transition_probs = self.transition_matrix[idx]
        next_state_index = np.random.choice(len(self.states), p=transition_probs)
        self.current_state = self.states[next_state_index]
        return self.current_state

# Definir la matriz de transición y los estados
transition_matrix = [
    [0.7, 0.3],
    [0.4, 0.6]
]
states = np.array(['Sunny', 'Rainy'])

# Crear una instancia de la cadena de Markov
mc = MarkovChain(transition_matrix, states)

# Realizar transiciones y mostrar el estado actual
print("Estado inicial:", mc.current_state)
for _ in range(5):
    mc.next_state()
    print("Siguiente estado:", mc.current_state)
