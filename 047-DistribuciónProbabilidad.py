#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

# Definir los eventos y sus probabilidades
eventos = ['A', 'B', 'C', 'D']
probabilidades = [0.2, 0.3, 0.4, 0.1]

# Generar una muestra de eventos según la distribución de probabilidad
muestra = np.random.choice(eventos, size=1000, p=probabilidades)

# Contar la frecuencia de cada evento en la muestra
frecuencia = {evento: np.sum(muestra == evento) for evento in eventos}

# Calcular la distribución de probabilidad
distribucion = {evento: freq / 1000 for evento, freq in frecuencia.items()}

# Imprimir resultados
print("Distribución de probabilidad:")
for evento, probabilidad in distribucion.items():
    print(f"{evento}: {probabilidad:.3f}")
