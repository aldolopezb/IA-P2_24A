#Aldo López Barrios
#21310106
#--------------------------
class ConditionalPlanner:
    def __init__(self, domain, initial_state, goal_state):
        self.domain = domain  # Dominio de la planificación condicional
        self.initial_state = initial_state  # Estado inicial
        self.goal_state = goal_state  # Estado meta
        self.plan = []  # Plan resultante

    def planificar(self):
        current_state = self.initial_state.copy()
        self.plan = []
        while not self._estado_coincide(current_state, self.goal_state):
            accion = self._seleccionar_accion(current_state)
            if accion is None:
                return None  # No se puede encontrar una solución
            self.plan.append(accion)
            self._aplicar_efectos(accion, current_state)
        return self.plan

    def _seleccionar_accion(self, current_state):
        for accion in self.domain:
            if self._precondiciones_cumplidas(accion, current_state):
                return accion
        return None  # No se puede encontrar una acción adecuada

    def _precondiciones_cumplidas(self, accion, current_state):
        for precondicion in accion['precondiciones']:
            if precondicion not in current_state or not current_state[precondicion]:
                return False
        return True

    def _aplicar_efectos(self, accion, current_state):
        for efecto in accion['efectos']:
            current_state[efecto] = True

    def _estado_coincide(self, state1, state2):
        for key in state2:
            if key not in state1 or state1[key] != state2[key]:
                return False
        return True

# Ejemplo de uso
if __name__ == "__main__":
    # Definición del dominio de planificación condicional
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

    # Creación del planificador condicional
    planner = ConditionalPlanner(domain, initial_state, goal_state)

    # Ejecución de la planificación
    plan = planner.planificar()

    # Imprimir el plan resultante
    if plan:
        print("Plan encontrado:")
        for accion in plan:
            print(accion['nombre'])
    else:
        print("No se encontró solución.")
