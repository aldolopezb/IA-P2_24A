import numpy as np
import gym

def q_learning(env, num_episodios, tasa_aprendizaje=0.8, factor_descuento=0.95, epsilon=0.1):
    # Inicializar la tabla Q con ceros
    num_estados = env.observation_space.n
    num_acciones = env.action_space.n
    q_table = np.zeros((num_estados, num_acciones))

    for episodio in range(num_episodios):
        estado = env.reset()
        done = False

        while not done:
            # Elegir la acción según epsilon-greedy
            if np.random.uniform(0, 1) < epsilon:
                accion = env.action_space.sample()  # Acción aleatoria
            else:
                accion = np.argmax(q_table[estado])  # Acción con mayor valor Q

            # Tomar la acción y observar el siguiente estado y la recompensa
            proximo_estado, recompensa, done, _ = env.step(accion)

            # Actualizar el valor Q del estado actual y la acción tomada
            q_value = q_table[estado, accion]
            max_q_next = np.max(q_table[proximo_estado])  # Valor Q máximo del siguiente estado
            new_q_value = (1 - tasa_aprendizaje) * q_value + tasa_aprendizaje * (recompensa + factor_descuento * max_q_next)
            q_table[estado, accion] = new_q_value

            estado = proximo_estado

    return q_table

# Crear el entorno FrozenLake-v1
env = gym.make('FrozenLake-v1')

# Definir los parámetros del Q-Learning
num_episodios = 1000

# Ejecutar Q-Learning
q_table = q_learning(env, num_episodios)

# Imprimir la tabla Q aprendida
print("Tabla Q aprendida:")
print(q_table)
