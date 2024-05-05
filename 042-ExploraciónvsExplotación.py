import numpy as np

class EpsilonGreedy:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def seleccionar_accion(self, q_values):
        if np.random.rand() < self.epsilon:
            # Exploración: selecciona una acción aleatoria
            return np.random.randint(len(q_values))
        else:
            # Explotación: selecciona la acción con el valor Q más alto
            return np.argmax(q_values)

# Ejemplo de uso
epsilon_greedy = EpsilonGreedy(0.1)  # Epsilon de 0.1 para un 10% de exploración

# Supongamos que tenemos valores Q para cuatro acciones
q_values = [1.2, 0.8, 1.5, 1.0]

# Seleccionamos una acción utilizando el enfoque epsilon-greedy
accion_seleccionada = epsilon_greedy.seleccionar_accion(q_values)

print("Valores Q:", q_values)
print("Acción seleccionada:", accion_seleccionada)
