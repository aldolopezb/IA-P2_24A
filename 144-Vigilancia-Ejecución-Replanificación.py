#Aldo López Barrios
#21310106
#--------------------------
class ExecutionMonitor:
    def __init__(self, initial_plan):
        self.initial_plan = initial_plan
        self.current_plan = initial_plan

    def monitor_execution(self, current_state):
        # Aquí se simularía la monitorización de la ejecución.
        # Podemos suponer que recibimos el estado actual y comparamos con el plan actual.
        # Si detectamos desviaciones o problemas en la ejecución, activamos la replanificación.
        deviation_detected = False  # Supongamos que no se detecta ninguna desviación por ahora
        if deviation_detected:
            return True  # Activar la replanificación
        else:
            return False  # No es necesario replanificar

class Replanner:
    def __init__(self, domain, initial_state, goal_state):
        self.domain = domain
        self.initial_state = initial_state
        self.goal_state = goal_state

    def replanificar(self):
        # Aquí implementaríamos el proceso de replanificación utilizando el dominio, el estado inicial y el estado meta.
        # Podemos utilizar un algoritmo de planificación como A* o cualquier otro método que se ajuste a nuestras necesidades.
        new_plan = []  # Por ahora, simplemente devolvemos una lista vacía como plan de replanificación
        return new_plan

# Ejemplo de uso
if __name__ == "__main__":
    # Definición del dominio de planificación
    domain = [
        {'nombre': 'limpiar_suelo', 'precondiciones': [], 'efectos': ['suelo_limpiado']},
        {'nombre': 'limpiar_mesas', 'precondiciones': [], 'efectos': ['mesas_limpiadas']},
        {'nombre': 'mover_silla', 'precondiciones': [], 'efectos': ['silla_movida']},
        {'nombre': 'mover_mesa', 'precondiciones': [], 'efectos': ['mesa_movida']},
        {'nombre': 'cargar_silla', 'precondiciones': [], 'efectos': ['silla_cargada']},
        {'nombre': 'cargar_mesa', 'precondiciones': [], 'efectos': ['mesa_cargada']}
    ]

    # Estado inicial
    initial_state = {
        'suelo_limpiado': False,
        'mesas_limpiadas': False,
        'silla_movida': False,
        'mesa_movida': False,
        'silla_cargada': False,
        'mesa_cargada': False
    }

    # Estado meta
    goal_state = {
        'suelo_limpiado': True,
        'mesas_limpiadas': True,
        'silla_movida': True,
        'mesa_movida': True,
        'silla_cargada': True,
        'mesa_cargada': True
    }

    # Creación del plan inicial (por ejemplo, obtenido mediante un planificador)
    initial_plan = [
        {'nombre': 'limpiar_suelo', 'efectos': ['suelo_limpiado']},
        {'nombre': 'limpiar_mesas', 'efectos': ['mesas_limpiadas']},
        {'nombre': 'mover_silla', 'efectos': ['silla_movida']},
        {'nombre': 'mover_mesa', 'efectos': ['mesa_movida']},
        {'nombre': 'cargar_silla', 'efectos': ['silla_cargada']},
        {'nombre': 'cargar_mesa', 'efectos': ['mesa_cargada']}
    ]

    # Creación del monitor de ejecución
    monitor = ExecutionMonitor(initial_plan)

    # Ejecución simulada del plan
    current_state = initial_state  # Supongamos que iniciamos desde el estado inicial
    replanificacion_activada = False
    while not replanificacion_activada and not monitor.current_plan == []:
        # Ejecutar la acción actual en el plan
        accion_actual = monitor.current_plan.pop(0)
        print(f"Ejecutando acción: {accion_actual['nombre']}")
        # Aquí se simularía la ejecución de la acción, actualizando el estado actual según los efectos de la acción.
        # Supongamos que estamos simulando la actualización del estado.
        current_state[accion_actual['efectos'][0]] = True  # Actualizamos el estado según los efectos de la acción
        # Monitorizar la ejecución actual y activar la replanificación si es necesario
        replanificacion_activada = monitor.monitor_execution(current_state)
    
    # Replanificar si es necesario
    if replanificacion_activada:
        replanificador = Replanner(domain, current_state, goal_state)
        new_plan = replanificador.replanificar()
        if new_plan:
            print("Se ha generado un nuevo plan:")
            for accion in new_plan:
                print(accion['nombre'])
        else:
            print("No se pudo generar un nuevo plan.")
    else:
        print("La ejecución se completó sin necesidad de replanificar.")
