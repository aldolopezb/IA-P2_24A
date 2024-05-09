#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

# Función para calcular la incertidumbre utilizando Monte Carlo
def monte_carlo_uncertainty(func, samples=1000):
    # Generar muestras aleatorias
    random_samples = np.random.normal(loc=0.0, scale=1.0, size=samples)
    # Calcular la función para cada muestra
    results = func(random_samples)
    # Calcular la media y la desviación estándar de los resultados
    mean_result = np.mean(results)
    std_dev_result = np.std(results)
    return mean_result, std_dev_result

# Función de ejemplo para la cual se calculará la incertidumbre
def example_function(x):
    return np.sin(x) + np.cos(2*x)

# Calcular la incertidumbre de la función de ejemplo utilizando Monte Carlo
mean_result, std_dev_result = monte_carlo_uncertainty(example_function)

# Imprimir los resultados
print("Media del resultado:", mean_result)
print("Desviación estándar del resultado:", std_dev_result)
