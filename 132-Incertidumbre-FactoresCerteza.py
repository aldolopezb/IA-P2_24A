#Aldo López Barrios
#21310106
#--------------------------
class ReglaConIncertidumbre:
    def __init__(self, antecedente, consecuente, factor_certeza):
        self.antecedente = antecedente
        self.consecuente = consecuente
        self.factor_certeza = factor_certeza

    def aplicable(self, hechos):
        return all(h in hechos for h in self.antecedente)

    def __repr__(self):
        return f"{self.antecedente} => {self.consecuente} ({self.factor_certeza})"

class SistemaConIncertidumbre:
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
                    print(f"Se agrega {regla.consecuente} basado en la regla {regla} y su factor de certeza")

# Crear un sistema de razonamiento con incertidumbre
sistema = SistemaConIncertidumbre()

# Agregar hechos iniciales
sistema.agregar_hecho("tiene_plumas")
sistema.agregar_hecho("es_pequeño")

# Agregar reglas con incertidumbre
regla1 = ReglaConIncertidumbre(["tiene_plumas"], "es un ave", 0.7)
regla2 = ReglaConIncertidumbre(["es_pequeño"], "es un ave", 0.5)
sistema.agregar_regla(regla1)
sistema.agregar_regla(regla2)

# Realizar el razonamiento
sistema.razonar()
