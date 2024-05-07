#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definir el universo del conjunto difuso
x = np.arange(0, 11, 1)

# Definir las funciones de membresía
bajo = fuzz.trimf(x, [0, 0, 5])
medio = fuzz.trimf(x, [0, 5, 10])
alto = fuzz.trimf(x, [5, 10, 10])

# Visualizar las funciones de membresía
plt.plot(x, bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(x, medio, 'g', linewidth=1.5, label='Medio')
plt.plot(x, alto, 'r', linewidth=1.5, label='Alto')
plt.title('Conjuntos Difusos')
plt.ylabel('Pertenencia')
plt.xlabel('Valor')
plt.legend(loc='center right')
plt.show()
