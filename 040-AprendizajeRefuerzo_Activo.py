import numpy as np

def aprendizaje_refuerzo_activo(num_estados, num_acciones, num_episodios, matriz_recompensas, factor_descuento, tasa_aprendizaje, epsilon):
    # Inicializar los valores Q
    valores_Q = np.zeros((num_estados, num_acciones))

    for _ in range(num_episodios):
        estado_actual = np.random.randint(num_estados)  # Inicializar el estado actual al azar

        while True:
            # Elegir la próxima acción basada en la política epsilon-greedy
            if np.random.rand() < epsilon:
                accion_elegida = np.random.randint(num_acciones)  # Acción aleatoria
            else:
                accion_elegida = np.argmax(valores_Q[estado_actual])  # Mejor acción según los valores Q

            # Obtener la recompensa para la acción elegida en el estado actual
            recompensa = matriz_recompensas[estado_actual, accion_elegida]

            # Obtener el próximo estado
            proximo_estado = np.random.randint(num_estados)

            # Actualizar el valor Q del estado actual y la acción elegida
            mejor_valor_Q = np.max(valores_Q[proximo_estado])
            valores_Q[estado_actual, accion_elegida] += tasa_aprendizaje * (recompensa + factor_descuento * mejor_valor_Q - valores_Q[estado_actual, accion_elegida])

            estado_actual = proximo_estado

            if estado_actual == num_estados - 1:  # Si llegamos al estado final, terminar el episodio
                break

    return valores_Q

# Ejemplo de uso
num_estados = 5
num_acciones = 2
num_episodios = 1000
matriz_recompensas = np.array([[0, 1],
                                [1, 0],
                                [0, 1],
                                [1, 0],
                                [1, 0]])
factor_descuento = 0.9
tasa_aprendizaje = 0.1
epsilon = 0.1

valores_Q = aprendizaje_refuerzo_activo(num_estados, num_acciones, num_episodios, matriz_recompensas, factor_descuento, tasa_aprendizaje, epsilon)
print("Valores Q aprendidos:")
print(valores_Q)
