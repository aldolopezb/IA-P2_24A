#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

class FiltroKalman:
    def __init__(self, initial_state, initial_covariance, transition_matrix, observation_matrix, process_noise_covariance, observation_noise_covariance):
        self.state = initial_state
        self.covariance = initial_covariance
        self.transition_matrix = transition_matrix
        self.observation_matrix = observation_matrix
        self.process_noise_covariance = process_noise_covariance
        self.observation_noise_covariance = observation_noise_covariance

    def predict(self):
        self.state = np.dot(self.transition_matrix, self.state)
        self.covariance = np.dot(np.dot(self.transition_matrix, self.covariance), self.transition_matrix.T) + self.process_noise_covariance

    def update(self, observation):
        observation_residual = observation - np.dot(self.observation_matrix, self.state)
        observation_residual_covariance = np.dot(np.dot(self.observation_matrix, self.covariance), self.observation_matrix.T) + self.observation_noise_covariance
        kalman_gain = np.dot(np.dot(self.covariance, self.observation_matrix.T), np.linalg.inv(observation_residual_covariance))
        self.state = self.state + np.dot(kalman_gain, observation_residual)
        self.covariance = np.dot((np.eye(self.state.shape[0]) - np.dot(kalman_gain, self.observation_matrix)), self.covariance)

# Definir los parámetros del filtro de Kalman
initial_state = np.array([0, 0])  # Estado inicial
initial_covariance = np.eye(2)     # Covarianza inicial
transition_matrix = np.array([[1, 1], [0, 1]])  # Matriz de transición
observation_matrix = np.array([[1, 0]])         # Matriz de observación
process_noise_covariance = np.eye(2) * 0.01     # Covarianza del ruido del proceso
observation_noise_covariance = np.eye(1) * 0.1  # Covarianza del ruido de observación

# Crear una instancia del filtro de Kalman
kalman_filter = FiltroKalman(initial_state, initial_covariance, transition_matrix, observation_matrix, process_noise_covariance, observation_noise_covariance)

# Realizar predicciones y actualizaciones
observations = [1, 2, 3, 4, 5]  # Observaciones
for observation in observations:
    kalman_filter.predict()
    kalman_filter.update(np.array([observation]))

# Imprimir el estado estimado final
print("Estado estimado final:", kalman_filter.state)
