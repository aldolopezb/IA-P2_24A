#Aldo López Barrios
#21310106
#--------------------------
class RazonamientoNoMonotónico:
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

class ReglaNoMonotónica:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

    def aplicable(self, hechos):
        return all(h in hechos for h in self.antecedente)

    def __repr__(self):
        return f"{self.antecedente} => {self.consecuente}"


# Crear un sistema de razonamiento no monotónico
sistema = RazonamientoNoMonotónico()

# Agregar hechos iniciales
sistema.agregar_hecho("puede_volar")
sistema.agregar_hecho("tiene_plumas")

# Agregar reglas
regla1 = ReglaNoMonotónica(["puede_volar", "tiene_plumas"], "es un pájaro")
sistema.agregar_regla(regla1)

# Realizar el razonamiento
sistema.razonar()

# Agregar un hecho nuevo
sistema.agregar_hecho("es un pájaro")

# Realizar el razonamiento nuevamente
sistema.razonar()
