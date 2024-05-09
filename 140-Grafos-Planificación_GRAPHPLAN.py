#Aldo López Barrios
#21310106
#--------------------------
from itertools import combinations

class GraphPlan:
    def __init__(self, acciones, estado_inicial, estado_meta):
        """
        Inicializa el planificador GRAPHPLAN con las acciones disponibles, el estado inicial y el estado meta.
        """
        self.acciones = acciones
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta
        self.grafo = {}
        self.nivel = 0

    def _aplicar_accion(self, estado, accion):
        """
        Aplica una acción al estado actual y devuelve el nuevo estado.
        """
        nuevo_estado = set(estado)
        for precondicion in accion['precondiciones']:
            if precondicion not in estado:
                return None  # La acción no se puede aplicar
        for efecto in accion['efectos']:
            nuevo_estado.add(efecto)
        return frozenset(nuevo_estado)

    def _es_mutex(self, capa, a1, a2):
        """
        Comprueba si dos acciones son mutuamente excluyentes en una capa dada del grafo.
        """
        for s1, s2 in combinations(capa, 2):
            if (a1, a2) in self.grafo['mutex'][s1] or (a2, a1) in self.grafo['mutex'][s1] or \
               (a1, a2) in self.grafo['mutex'][s2] or (a2, a1) in self.grafo['mutex'][s2]:
                return True
        return False

    def _expandir(self):
        """
        Expande el grafo añadiendo una nueva capa de acciones y estados.
        """
        self.grafo[self.nivel] = {'acciones': set(), 'estado': set(), 'mutex': {}}
        self.grafo[self.nivel]['estado'].add(self.estado_inicial)
        for accion in self.acciones:
            if self._aplicar_accion(self.estado_inicial, accion):
                self.grafo[self.nivel]['acciones'].add(accion['nombre'])
        if self.nivel > 0:  # Verificar si estamos en el primer nivel
            for capa in range(self.nivel):
                self.grafo[self.nivel]['mutex'][capa] = set()
                for a1 in self.grafo[capa]['acciones']:
                    for a2 in self.grafo[capa]['acciones']:
                        if self._es_mutex(capa, a1, a2):
                            self.grafo[self.nivel]['mutex'][capa].add((a1, a2))
        self.nivel += 1

    def planificar(self):
        """
        Ejecuta el algoritmo GRAPHPLAN hasta encontrar una solución o determinar que no existe.
        """
        while True:
            self._expandir()
            if self.estado_meta in self.grafo[self.nivel - 1]['estado']:
                return self._extraer_solucion()
            if self.grafo[self.nivel - 1] == self.grafo[self.nivel - 2]:
                return None  # No se encontró solución

    def _extraer_solucion(self):
        """
        Extrae la solución del grafo planificado.
        """
        solucion = []
        for nivel in range(self.nivel - 1, -1, -1):
            acciones_aplicables = []
            for accion in self.grafo[nivel]['acciones']:
                if accion in self.grafo[nivel]['estado']:
                    acciones_aplicables.append(accion)
            solucion.insert(0, acciones_aplicables)
            for capa in range(nivel + 1, self.nivel):
                for accion in solucion[0]:
                    if any((accion, otra_accion) in self.grafo[nivel]['mutex'][capa] or \
                           (otra_accion, accion) in self.grafo[nivel]['mutex'][capa] for otra_accion in self.grafo[nivel]['acciones']):
                        solucion[0].remove(accion)
                        break
        return solucion

# Ejemplo de uso
if __name__ == "__main__":
    # Definición de acciones
    acciones = [
        {'nombre': 'limpiar', 'precondiciones': frozenset(), 'efectos': frozenset({'limpio'})},
        {'nombre': 'mover', 'precondiciones': frozenset({'limpio'}), 'efectos': frozenset({'en_posicion'})},
        {'nombre': 'cargar', 'precondiciones': frozenset({'en_posicion'}), 'efectos': frozenset({'cargado'})}
    ]

    # Definición de estado inicial
    estado_inicial = frozenset({'robot'})

    # Definición del estado meta
    estado_meta = frozenset({'cargado'})

    # Creación del objeto GraphPlan
    planificador = GraphPlan(acciones, estado_inicial, estado_meta)

    # Ejecución del planificador
    plan = planificador.planificar()

    # Imprimir la solución
    if plan:
        print("Solución encontrada:")
        for nivel, acciones in enumerate(plan):
            print(f"Nivel {nivel}: {acciones}")
    else:
        print("No se encontró solución.")
