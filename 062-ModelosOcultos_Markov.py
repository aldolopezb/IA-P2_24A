#Aldo López Barrios
#21310106
#--------------------------
from hmmlearn import hmm
import numpy as np

# Definir el modelo HMM
modelo = hmm.MultinomialHMM(n_components=2)

# Definir las probabilidades de transición
modelo.transmat_ = np.array([[0.7, 0.3],
                             [0.4, 0.6]])

# Definir las probabilidades iniciales de los estados ocultos
modelo.startprob_ = np.array([0.5, 0.5])

# Definir las probabilidades de emisión
modelo.emissionprob_ = np.array([[0.1, 0.4, 0.5],
                                 [0.6, 0.3, 0.1]])

# Generar muestras del modelo
muestras, estados_ocultos = modelo.sample(n_samples=100, random_state=42)

# Estimar la secuencia de estados ocultos más probable para las observaciones
estados_ocultos_predichos = modelo.predict(muestras)

# Imprimir resultados
print("Muestras generadas:")
print(muestras)
print("\nEstados ocultos reales:")
print(estados_ocultos)
print("\nEstados ocultos predichos:")
print(estados_ocultos_predichos)
