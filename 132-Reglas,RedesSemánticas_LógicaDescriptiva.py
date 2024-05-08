#Aldo López Barrios
#21310106
#--------------------------
class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

    def __repr__(self):
        return f"{self.antecedente} -> {self.consecuente}"


class RedSemantica:
    def __init__(self):
        self.relaciones = {}

    def agregar_relacion(self, objeto1, relacion, objeto2):
        if objeto1 not in self.relaciones:
            self.relaciones[objeto1] = {}
        if relacion not in self.relaciones[objeto1]:
            self.relaciones[objeto1][relacion] = []
        self.relaciones[objeto1][relacion].append(objeto2)

    def __repr__(self):
        return str(self.relaciones)


# Definir algunas reglas
regla_1 = Regla("si hace frío", "entonces llevar abrigo")
regla_2 = Regla("si hay tráfico", "entonces salir más temprano")
regla_3 = Regla("si hay lluvia", "entonces llevar paraguas")

# Mostrar las reglas
print("Reglas:")
print(regla_1)
print(regla_2)
print(regla_3)

# Definir una red semántica
red_semantica = RedSemantica()
red_semantica.agregar_relacion("gato", "es un", "animal")
red_semantica.agregar_relacion("gato", "tiene", "pelaje")
red_semantica.agregar_relacion("perro", "es un", "animal")
red_semantica.agregar_relacion("perro", "tiene", "cola")

# Mostrar la red semántica
print("\nRed Semántica:")
print(red_semantica)
