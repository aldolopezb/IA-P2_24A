import numpy as np

def aprendizaje_refuerzo_pasivo(num_estados, num_acciones, num_episodios, matriz_recompensas, tasa_aprendizaje):
    # Inicializar los valores de acción
    valores_accion = np.zeros((num_estados, num_acciones))

    for _ in range(num_episodios):
        estado_actual = np.random.randint(num_estados)  # Inicializar el estado actual al azar
        accion_elegida = np.random.randint(num_acciones)  # Elegir una acción al azar

        while True:
            # Obtener la recompensa para la acción elegida en el estado actual
            recompensa = matriz_recompensas[estado_actual, accion_elegida]
            
            # Actualizar el valor de la acción elegida en el estado actual
            valores_accion[estado_actual, accion_elegida] += tasa_aprendizaje * (recompensa - valores_accion[estado_actual, accion_elegida])

            # Moverse al siguiente estado de forma aleatoria
            estado_actual = np.random.randint(num_estados)

            # Elegir una nueva acción al azar
            accion_elegida = np.random.randint(num_acciones)

            if estado_actual == num_estados - 1:  # Si llegamos al estado final, terminar el episodio
                break

    return valores_accion

# Ejemplo de uso
num_estados = 5
num_acciones = 2
num_episodios = 1000
matriz_recompensas = np.array([[0, 1],
                                [1, 0],
                                [0, 1],
                                [1, 0],
                                [1, 0]])
tasa_aprendizaje = 0.1

valores_accion = aprendizaje_refuerzo_pasivo(num_estados, num_acciones, num_episodios, matriz_recompensas, tasa_aprendizaje)
print("Valores de acción aprendidos:")
print(valores_accion)
