#Aldo López Barrios
#21310106
#--------------------------
import gym
import time

# Crear el entorno
env = gym.make('CartPole-v1')

# Reiniciar el entorno
observation = env.reset()

# Realizar un bucle de interacción
for _ in range(100):
    # Renderizar el entorno (opcional)
    env.render()

    # Simular una acción
    action = env.action_space.sample()  # Seleccionar una acción al azar
    step_info = env.step(action)

    # Extraer la observación, la recompensa, si el episodio ha terminado y la información adicional
    observation, reward, done, info = step_info[0], step_info[1], step_info[2], {}

    # Imprimir la observación (lectura del sensor)
    print("Observation (sensor reading):", observation)

    # Imprimir la recompensa (opcional)
    print("Reward:", reward)

    # Comprobar si el episodio ha terminado
    if done:
        print("Episode finished after", _+1, "timesteps")
        break

    # Introducir un pequeño retraso para simular el tiempo del mundo real
    time.sleep(0.1)

# Cerrar el entorno (opcional)
env.close()
