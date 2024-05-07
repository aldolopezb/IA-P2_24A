#Aldo López Barrios
#21310106
#--------------------------
class BaseConocimiento:
    def __init__(self):
        self.hechos = set()
        self.reglas = []

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def agregar_regla(self, regla):
        self.reglas.append(regla)

    def inferir(self):
        nuevos_hechos = set()

        for regla in self.reglas:
            if regla.evaluar(self.hechos):
                nuevos_hechos.add(regla.consecuencia)

        self.hechos.update(nuevos_hechos)

    def consultar(self, hecho):
        return hecho in self.hechos


class Regla:
    def __init__(self, antecedentes, consecuencia):
        self.antecedentes = antecedentes
        self.consecuencia = consecuencia

    def evaluar(self, hechos):
        for antecedente in self.antecedentes:
            if antecedente not in hechos:
                return False
        return True


# Crear una base de conocimiento
bc = BaseConocimiento()

# Agregar hechos
bc.agregar_hecho('pajaro_vuela')
bc.agregar_hecho('pajaro')
bc.agregar_hecho('pez_nada')
bc.agregar_hecho('pez')
bc.agregar_hecho('gato_maulla')
bc.agregar_hecho('gato')
bc.agregar_hecho('tiburon_come')

# Definir reglas
regla1 = Regla(['pajaro_vuela', 'pajaro'], 'animal_vuela')
regla2 = Regla(['pez_nada', 'pez'], 'animal_nada')
regla3 = Regla(['gato_maulla', 'gato'], 'animal_mamifero')
regla4 = Regla(['tiburon_come'], 'tiburon')

# Agregar reglas a la base de conocimiento
bc.agregar_regla(regla1)
bc.agregar_regla(regla2)
bc.agregar_regla(regla3)
bc.agregar_regla(regla4)

# Realizar inferencias
bc.inferir()

# Consultar hechos
print(bc.consultar('animal_vuela'))  # True
print(bc.consultar('animal_nada'))   # True
print(bc.consultar('animal_mamifero'))  # True
print(bc.consultar('tiburon'))       # True
print(bc.consultar('animal_terrestre'))  # False
