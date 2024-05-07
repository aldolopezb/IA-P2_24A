#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
from scipy.linalg import block_diag

class FiltroKalman:
    def __init__(self, A, B, H, Q, R, x0, P0):
        self.A = A  # Matriz de transición de estado
        self.B = B  # Matriz de control
        self.H = H  # Matriz de observación
        self.Q = Q  # Covarianza del proceso de estado
        self.R = R  # Covarianza del ruido de medición
        self.x = x0  # Estado inicial
        self.P = P0  # Covarianza inicial del estado

    def predict(self, u=None):
        # Predicción del estado
        self.x = np.dot(self.A, self.x)
        if u is not None:
            self.x += np.dot(self.B, u)
        # Predicción de la covarianza del estado
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q

    def update(self, z):
        # Innovación
        y = z - np.dot(self.H, self.x)
        # Residual de covarianza
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R
        # Ganancia de Kalman
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        # Actualización del estado
        self.x += np.dot(K, y)
        # Actualización de la covarianza del estado
        I = np.eye(self.P.shape[0])
        self.P = np.dot(I - np.dot(K, self.H), self.P)

# Definir las matrices del modelo
dt = 1.0  # Paso de tiempo
A = np.array([[1, dt], [0, 1]])  # Matriz de transición de estado
B = np.array([[0], [0]])  # Matriz de control
H = np.array([[1, 0]])  # Matriz de observación
Q = 0.01 * np.eye(2)  # Covarianza del proceso de estado
R = 0.1  # Covarianza del ruido de medición
x0 = np.array([0, 0])  # Estado inicial
P0 = np.eye(2)  # Covarianza inicial del estado

# Crear el filtro de Kalman
filtro_kalman = FiltroKalman(A, B, H, Q, R, x0, P0)

# Generar una secuencia de observaciones
observaciones = [0.5, 1.0, 1.5, 2.0]

# Realizar la predicción y actualización para cada observación
for z in observaciones:
    filtro_kalman.predict()
    filtro_kalman.update(z)
    print("Predicción:", filtro_kalman.x)
    print("Covarianza de predicción:", filtro_kalman.P)
    print("Observación:", z)
