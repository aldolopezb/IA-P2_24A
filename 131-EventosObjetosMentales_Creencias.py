#Aldo López Barrios
#21310106
#--------------------------
class Creencia:
    def __init__(self, sujeto, predicado, objeto):
        self.sujeto = sujeto
        self.predicado = predicado
        self.objeto = objeto

    def __repr__(self):
        return f"{self.sujeto} {self.predicado} {self.objeto}"


# Definir algunas creencias
creencia_1 = Creencia("Juan", "cree que", "el cielo es azul")
creencia_2 = Creencia("María", "cree que", "los gatos son adorables")
creencia_3 = Creencia("Pedro", "cree que", "el café es bueno")

# Mostrar las creencias
print("Creencias:")
print(creencia_1)
print(creencia_2)
print(creencia_3)
