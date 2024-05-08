#Aldo López Barrios
#21310106
#--------------------------
class SistemaExperto:
    def __init__(self):
        self.hechos = set()
        self.reglas = []

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def agregar_regla(self, regla):
        self.reglas.append(regla)

    def razonar(self):
        for regla in self.reglas:
            if regla.aplicable(self.hechos):
                if regla.consecuente not in self.hechos:
                    self.hechos.add(regla.consecuente)
                    print(f"Se agrega {regla.consecuente} basado en la regla {regla}")

class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

    def aplicable(self, hechos):
        return all(h in hechos for h in self.antecedente)

    def __repr__(self):
        return f"{self.antecedente} => {self.consecuente}"

# Crear un sistema experto
sistema_experto = SistemaExperto()

# Agregar hechos iniciales
sistema_experto.agregar_hecho("tiene_plumas")
sistema_experto.agregar_hecho("es_pequeño")

# Agregar reglas
regla1 = Regla(["tiene_plumas"], "es un ave")
regla2 = Regla(["es_pequeño"], "es un ave")
sistema_experto.agregar_regla(regla1)
sistema_experto.agregar_regla(regla2)

# Realizar el razonamiento
sistema_experto.razonar()
