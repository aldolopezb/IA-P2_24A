#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

def sigmoid(x):
    """Función de activación sigmoidal."""
    return 1 / (1 + np.exp(-x))

def relu(x):
    """Función de activación ReLU."""
    return np.maximum(0, x)

def tanh(x):
    """Función de activación tangente hiperbólica."""
    return np.tanh(x)

def softmax(x):
    """Función de activación softmax."""
    exp_x = np.exp(x - np.max(x))  # Evitar overflow
    return exp_x / np.sum(exp_x)

# Ejemplo de uso
if __name__ == "__main__":
    # Entrada de ejemplo
    entrada = np.array([-1, 0, 1])

    # Aplicar las funciones de activación a la entrada
    salida_sigmoid = sigmoid(entrada)
    salida_relu = relu(entrada)
    salida_tanh = tanh(entrada)
    salida_softmax = softmax(entrada)

    # Imprimir las salidas
    print("Salida de la función sigmoidal:", salida_sigmoid)
    print("Salida de la función ReLU:", salida_relu)
    print("Salida de la función tangente hiperbólica:", salida_tanh)
    print("Salida de la función softmax:", salida_softmax)
