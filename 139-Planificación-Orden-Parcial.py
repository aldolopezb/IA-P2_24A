#Aldo López Barrios
#21310106
#--------------------------
class Accion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.precondiciones = set()
        self.efectos = set()

    def agregar_precondicion(self, precondicion):
        self.precondiciones.add(precondicion)

    def agregar_efecto(self, efecto):
        self.efectos.add(efecto)

    def es_aplicable(self, estado):
        return all(precondicion in estado for precondicion in self.precondiciones)

    def aplicar(self, estado):
        nuevo_estado = set(estado)
        nuevo_estado.update(self.efectos)
        return nuevo_estado


class PlanificadorOrdenParcial:
    def __init__(self, acciones, estado_inicial, estado_meta):
        self.acciones = acciones
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta

    def planificar(self):
        plan = []
        estado_actual = set(self.estado_inicial)
        while estado_actual != self.estado_meta:
            accion_aplicable = None
            for accion in self.acciones:
                if accion.es_aplicable(estado_actual):
                    accion_aplicable = accion
                    break
            if accion_aplicable:
                plan.append(accion_aplicable)
                estado_actual = accion_aplicable.aplicar(estado_actual)
            else:
                raise Exception("No se pudo encontrar una acción aplicable")
        return plan


# Definir acciones
accion_a = Accion("A")
accion_a.agregar_efecto("b")
accion_a.agregar_efecto("c")

accion_b = Accion("B")
accion_b.agregar_efecto("d")

# Definir estado inicial y estado meta
estado_inicial = {"a"}
estado_meta = {"b", "c", "d"}

# Planificar
planificador = PlanificadorOrdenParcial([accion_a, accion_b], estado_inicial, estado_meta)
plan = planificador.planificar()

# Imprimir plan
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print(f"- {accion.nombre}")
else:
    print("No se pudo encontrar un plan")
