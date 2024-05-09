#Aldo López Barrios
#21310106
#--------------------------
class GramaticaChomsky:
    def __init__(self):
        self.tipo_0 = []
        self.tipo_1 = []
        self.tipo_2 = []
        self.tipo_3 = []

    def agregar_tipo_0(self, reglas):
        self.tipo_0.extend(reglas)

    def agregar_tipo_1(self, reglas):
        self.tipo_1.extend(reglas)

    def agregar_tipo_2(self, reglas):
        self.tipo_2.extend(reglas)

    def agregar_tipo_3(self, reglas):
        self.tipo_3.extend(reglas)

# Ejemplo de uso
gramatica = GramaticaChomsky()

# Definir reglas para cada tipo de gramática
gramatica.agregar_tipo_0([
    "S -> 0S1",
    "S -> 1S0",
    "S -> 01"
])

gramatica.agregar_tipo_1([
    "S -> aS",
    "S -> bS",
    "S -> c"
])

gramatica.agregar_tipo_2([
    "S -> aA",
    "A -> b"
])

gramatica.agregar_tipo_3([
    "S -> aA",
    "A -> a"
])

# Imprimir las reglas de cada tipo de gramática
print("Gramática Tipo 0:")
for regla in gramatica.tipo_0:
    print(regla)

print("\nGramática Tipo 1:")
for regla in gramatica.tipo_1:
    print(regla)

print("\nGramática Tipo 2:")
for regla in gramatica.tipo_2:
    print(regla)

print("\nGramática Tipo 3:")
for regla in gramatica.tipo_3:
    print(regla)
