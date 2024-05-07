#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
from hmmlearn import hmm

# Definir el modelo HMM
model = hmm.GaussianHMM(n_components=3, covariance_type="full")

# Establecer los parámetros del modelo (probabilidades de transición y emisión)
model.startprob_ = np.array([0.6, 0.3, 0.1])  # Probabilidades iniciales de los estados ocultos
model.transmat_ = np.array([[0.7, 0.2, 0.1],   # Matriz de transición entre estados ocultos
                            [0.3, 0.5, 0.2],
                            [0.3, 0.3, 0.4]])
model.means_ = np.array([[0.0, 0.0],           # Medias de las distribuciones gaussianas de los estados ocultos
                         [3.0, -3.0],
                         [5.0, 10.0]])
model.covars_ = np.tile(np.identity(2), (3, 1, 1))  # Covarianzas de las distribuciones gaussianas

# Generar muestras a partir del modelo
X, Z = model.sample(100)

# Imprimir las muestras y los estados ocultos correspondientes
print("Muestras generadas:")
print(X)
print("Estados ocultos correspondientes:")
print(Z)
