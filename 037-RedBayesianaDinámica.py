#Aldo López Barrios
#21310106
#--------------------------

import numpy as np

class DynamicBayesianNetwork:
    def __init__(self, num_states, num_actions):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transition_model = np.zeros((num_states, num_states, num_actions))  # T(s, s', a)
        self.observation_model = np.zeros((num_states, num_actions))  # O(s', a)
        self.reward_model = np.zeros((num_states, num_actions))  # R(s, a)

    def set_transition_model(self, transition_model):
        self.transition_model = transition_model

    def set_observation_model(self, observation_model):
        self.observation_model = observation_model

    def set_reward_model(self, reward_model):
        self.reward_model = reward_model

    def infer_state(self, observation_sequence):
        # Inferir el estado más probable dado una secuencia de observaciones
        pass

# Ejemplo de uso
num_states = 3
num_actions = 2
dbn = DynamicBayesianNetwork(num_states, num_actions)

# Definir modelos
transition_model = np.array([[[0.7, 0.2, 0.1],
                              [0.1, 0.6, 0.3],
                              [0.3, 0.3, 0.4]],
                             
                             [[0.6, 0.3, 0.1],
                              [0.2, 0.5, 0.3],
                              [0.4, 0.3, 0.3]]])

observation_model = np.array([[0.9, 0.1],
                               [0.2, 0.8],
                               [0.5, 0.5]])

reward_model = np.array([[1, -1],
                         [2, 0],
                         [0, 1]])

dbn.set_transition_model(transition_model)
dbn.set_observation_model(observation_model)
dbn.set_reward_model(reward_model)

# Inferir el estado más probable dado una secuencia de observaciones
observation_sequence = [0, 1, 0]
inferred_state = dbn.infer_state(observation_sequence)
print("Estado inferido:", inferred_state)
