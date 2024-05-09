#Aldo López Barrios
#21310106
#--------------------------
class HTNPlanner:
    def __init__(self, domain, initial_state, tasks):
        self.domain = domain  # Dominio HTN
        self.initial_state = initial_state  # Estado inicial
        self.tasks = tasks  # Tareas a realizar
        self.plan = []  # Plan resultante

    def planificar(self):
        self.plan = self._planificar_tarea(self.tasks)

    def _planificar_tarea(self, tarea):
        if self._tarea_es_primitive(tarea):
            return [tarea]
        else:
            subplan = []
            subtasks = self._descomponer_tarea(tarea)
            for subtask in subtasks:
                subplan += self._planificar_tarea(subtask)
            return subplan

    def _tarea_es_primitive(self, tarea):
        return tarea in self.domain['primitivas']

    def _descomponer_tarea(self, tarea):
        return self.domain['descomposiciones'][tarea]

# Ejemplo de uso
if __name__ == "__main__":
    # Definición del dominio HTN
    domain = {
        'primitivas': ['limpiar', 'mover', 'cargar'],
        'descomposiciones': {
            'limpiar': ['limpiar_suelo', 'limpiar_mesas'],
            'mover': ['mover_silla', 'mover_mesa'],
            'cargar': ['cargar_silla', 'cargar_mesa']
        }
    }

    # Estado inicial
    initial_state = {
        'suelo_limpiado': False,
        'mesas_limpiadas': False,
        'silla_movida': False,
        'mesa_movida': False,
        'silla_cargada': False,
        'mesa_cargada': False
    }

    # Tarea principal
    tarea_principal = 'limpiar'

    # Creación del planificador HTN
    planner = HTNPlanner(domain, initial_state, tarea_principal)

    # Ejecución de la planificación
    planner.planificar()

    # Imprimir el plan resultante
    print("Plan resultante:")
    print(planner.plan)
