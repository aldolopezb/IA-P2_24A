#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

class Neurona:
    def __init__(self, num_entradas):
        # Inicializar los pesos y el sesgo de manera aleatoria
        self.pesos = np.random.rand(num_entradas)
        self.sesgo = np.random.rand()

    def activacion(self, entrada):
        # Función de activación (sigmoid)
        return 1 / (1 + np.exp(-np.dot(entrada, self.pesos) - self.sesgo))

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una neurona con 3 entradas
    neurona = Neurona(3)

    # Entradas de ejemplo
    entrada = np.array([0.5, 0.3, 0.2])

    # Calcular la salida de la neurona
    salida = neurona.activacion(entrada)

    print("Salida de la neurona:", salida)
