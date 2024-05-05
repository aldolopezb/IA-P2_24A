import gym
import numpy as np

def policy_iteration(env, num_iteraciones=1000):
    # Inicializar la tabla de valores de estado con ceros
    num_estados = env.observation_space.n
    valores = np.zeros(num_estados, dtype=float)

    for _ in range(num_iteraciones):
        # Inicializar la política aleatoria
        politica = np.random.randint(0, env.action_space.n, num_estados)

        # Evaluación de la política
        for _ in range(num_estados):
            estado = env.reset()
            done = False
            while not done:
                accion = politica[estado]
                proximo_estado, recompensa, done, _ = env.step(accion)
                valores[estado] += recompensa
                estado = proximo_estado

        # Mejora de la política
        for estado in range(num_estados):
            q_values = np.zeros(env.action_space.n)
            for accion in range(env.action_space.n):
                estado_siguiente, recompensa, done, _ = env.step(accion)
                q_values[accion] = recompensa + valores[estado_siguiente]
            politica[estado] = np.argmax(q_values)

    return politica

# Crear el entorno FrozenLake-v1
env = gym.make('FrozenLake-v1')

# Ejecutar la iteración de políticas
politica_optima = policy_iteration(env)

# Imprimir la política óptima
print("Política óptima:", politica_optima)
