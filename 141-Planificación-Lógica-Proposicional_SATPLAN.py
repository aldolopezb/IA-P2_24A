#Aldo López Barrios
#21310106
#--------------------------
from pysat.solvers import Glucose3

class SATPlan:
    def __init__(self, acciones, inicial, meta):
        self.acciones = acciones
        self.inicial = inicial
        self.meta = meta

    def codificar_acciones(self, solver, nivel):
        for accion in self.acciones:
            for precond in accion['precondiciones']:
                solver.add_clause([-self.inicial[precond][nivel]])  # La acción no puede aplicarse si la precondición no se cumple
                for efecto in accion['efectos']:
                    if efecto != precond:
                        solver.add_clause([self.inicial[precond][nivel] * -1, self.inicial[efecto][nivel], accion['nombre']])  # Si la precondición se cumple, el efecto no se anula

    def planificar(self):
        solver = Glucose3()
        nivel = 0
        while True:
            for var, val in self.inicial.items():
                solver.add_clause([val[nivel]])  # Añadir el estado actual al solver
            if self.meta in self.inicial.keys():  # Verificar si hemos alcanzado el estado meta
                solver.add_clause([self.inicial[self.meta][nivel]])
                break
            self.codificar_acciones(solver, nivel)
            if not solver.solve():  # No se puede alcanzar el estado meta
                return None
            else:
                nivel += 1

        plan = []
        while nivel > 0:
            for accion in self.acciones:
                if solver.get_model()[accion['nombre'] + nivel * 1000]:
                    plan.insert(0, accion['nombre'])
                    for precond in accion['precondiciones']:
                        for i in range(nivel):
                            if self.inicial[precond][i]:
                                nivel = i
                                break
                    break

        return plan

# Ejemplo de uso
if __name__ == "__main__":
    acciones = [
        {'nombre': 'limpiar', 'precondiciones': [], 'efectos': ['limpio']},
        {'nombre': 'mover', 'precondiciones': ['limpio'], 'efectos': ['en_posicion']},
        {'nombre': 'cargar', 'precondiciones': ['en_posicion'], 'efectos': ['cargado']}
    ]

    inicial = {'robot': [1], 'limpio': [2], 'en_posicion': [1], 'cargado': [1]}
    meta = 'cargado'

    planificador = SATPlan(acciones, inicial, meta)
    plan = planificador.planificar()

    if plan:
        print("Solución encontrada:")
        print(plan)
    else:
        print("No se encontró solución.")
