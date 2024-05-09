#Aldo López Barrios
#21310106
#--------------------------
class Estado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.transiciones = {}

    def agregar_transicion(self, estado_destino, accion):
        self.transiciones[accion] = estado_destino

    def obtener_destino(self, accion):
        return self.transiciones.get(accion)


class EspacioEstados:
    def __init__(self):
        self.estados = {}
        self.estado_inicial = None

    def agregar_estado(self, estado, es_inicial=False):
        self.estados[estado.nombre] = estado
        if es_inicial:
            self.estado_inicial = estado

    def obtener_estado(self, nombre):
        return self.estados.get(nombre)


# Crear estados
estado_a = Estado("A")
estado_b = Estado("B")
estado_c = Estado("C")

# Definir transiciones
estado_a.agregar_transicion(estado_b, "Ir a B")
estado_b.agregar_transicion(estado_c, "Ir a C")
estado_c.agregar_transicion(estado_a, "Volver a A")

# Crear espacio de estados
espacio_estados = EspacioEstados()
espacio_estados.agregar_estado(estado_a, es_inicial=True)
espacio_estados.agregar_estado(estado_b)
espacio_estados.agregar_estado(estado_c)

# Ejemplo de uso: obtener el destino de una transición desde el estado inicial
accion = "Ir a B"
destino = espacio_estados.estado_inicial.obtener_destino(accion)
if destino:
    print(f"Desde el estado inicial, al ejecutar la acción '{accion}', llegamos al estado '{destino.nombre}'")
else:
    print(f"No se encontró una transición válida para la acción '{accion}' desde el estado inicial")
