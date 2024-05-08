#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import medfilt

# Generar datos de ejemplo: señal con ruido
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 5 * t) + np.random.normal(0, 0.5, 1000)

# Aplicar filtro de mediana para eliminar el ruido
filtered_signal = medfilt(signal, kernel_size=5)

# Graficar la señal original y la señal filtrada
plt.figure(figsize=(10, 6))
plt.plot(t, signal, label='Señal Original', alpha=0.5)
plt.plot(t, filtered_signal, label='Señal Filtrada', color='red')
plt.title('Filtro de Mediana para Eliminar Ruido')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()
