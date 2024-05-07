#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

# Parámetros del proceso estacionario
mu = 2.0
sigma = 1.5
num_samples = 1000

# Generar muestras de una distribución normal
muestras = np.random.normal(mu, sigma, num_samples)

# Calcular la media y la varianza de las muestras
media = np.mean(muestras)
varianza = np.var(muestras)

print("Media:", media)
print("Varianza:", varianza)
