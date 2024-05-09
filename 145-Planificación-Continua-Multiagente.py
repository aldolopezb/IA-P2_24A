#Aldo López Barrios
#21310106
#--------------------------
class Agent:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.path = []

    def planificar_ruta(self, mapa):
        # Aquí implementaríamos el algoritmo de planificación de ruta para el agente, por ejemplo A*.
        # Supondremos que el mapa es una matriz 2D donde cada celda puede ser un obstáculo o estar libre.
        # El algoritmo debe calcular una ruta desde el punto de inicio hasta el objetivo evitando obstáculos.
        # Por ahora, supondremos que el agente simplemente va en línea recta hacia el objetivo.
        self.path = [self.start, self.goal]

class ContinuousPlanner:
    def __init__(self, agents):
        self.agents = agents

    def planificar(self, mapa):
        # Aquí implementaríamos el algoritmo de planificación continua, como MAPF.
        # En MAPF, se deben considerar múltiples agentes que pueden compartir caminos pero no celdas en el mismo momento.
        # Por ahora, simplemente vamos a planificar las rutas de los agentes secuencialmente.
        for agente in self.agents:
            agente.planificar_ruta(mapa)

# Ejemplo de uso
if __name__ == "__main__":
    # Creación de agentes
    agent1 = Agent((0, 0), (5, 5))
    agent2 = Agent((1, 1), (6, 6))
    agent3 = Agent((2, 2), (7, 7))

    # Creación del planificador continuo
    planner = ContinuousPlanner([agent1, agent2, agent3])

    # Definición del mapa
    mapa = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # Planificación de rutas para los agentes
    planner.planificar(mapa)

    # Impresión de las rutas planificadas
    for i, agente in enumerate([agent1, agent2, agent3]):
        print(f"Ruta del agente {i + 1}: {agente.path}")
