#Aldo López Barrios
#21310106
#--------------------------
from filterpy.monte_carlo import systematic_resample
import numpy as np

class ParticleFilter:
    def __init__(self, initial_particles, transition_function, observation_function, observation_noise_covariance):
        self.particles = initial_particles
        self.transition_function = transition_function
        self.observation_function = observation_function
        self.observation_noise_covariance = observation_noise_covariance

    def predict(self):
        for i in range(len(self.particles)):
            self.particles[i] = self.transition_function(self.particles[i])

    def update(self, observation):
        weights = []
        for particle in self.particles:
            predicted_observation = self.observation_function(particle)
            residual = observation - predicted_observation
            # Calcular la probabilidad de observación dado el estado (likelihood)
            weight = np.exp(-0.5 * np.dot(residual.T, np.linalg.solve(self.observation_noise_covariance, residual)))
            weights.append(weight)
        # Normalizar los pesos
        weights /= np.sum(weights)
        # Resampling sistemático
        indexes = systematic_resample(weights)
        self.particles = [self.particles[i] for i in indexes]

# Función de transición: Modelo de movimiento simple (caminar hacia adelante)
def transition_function(state):
    return state + np.random.normal(0, 1, state.shape)

# Función de observación: Modelo de observación simple (observar el estado directamente)
def observation_function(state):
    return state

# Definir los parámetros del filtro de partículas
num_particles = 100
initial_particles = np.random.normal(0, 1, (num_particles, 1))  # Generar partículas iniciales
observation_noise_covariance = np.eye(1) * 0.1  # Covarianza del ruido de observación

# Crear una instancia del filtro de partículas
particle_filter = ParticleFilter(initial_particles, transition_function, observation_function, observation_noise_covariance)

# Realizar la predicción y la actualización
observations = [1, 2, 3, 4, 5]  # Observaciones
for observation in observations:
    particle_filter.predict()
    particle_filter.update(np.array([observation]))

# Imprimir el estado estimado final (la media de las partículas)
estimated_state = np.mean(particle_filter.particles)
print("Estado estimado final:", estimated_state)
