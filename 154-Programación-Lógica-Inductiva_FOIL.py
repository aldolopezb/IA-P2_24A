#Aldo López Barrios
#21310106
#--------------------------
class FOIL:
    def __init__(self, ejemplos, predicado_objetivo):
        self.ejemplos = ejemplos
        self.predicado_objetivo = predicado_objetivo
        self.ejemplos_positivos = []
        self.ejemplos_negativos = []

    def separar_ejemplos(self):
        for ejemplo in self.ejemplos:
            if self.predicado_objetivo(ejemplo):
                self.ejemplos_positivos.append(ejemplo)
            else:
                self.ejemplos_negativos.append(ejemplo)

    def foil(self):
        self.separar_ejemplos()
        # Implementa el algoritmo FOIL aquí
        # Este es solo un esquema básico
        regla = "SI "
        for i, atributo in enumerate(self.ejemplos[0]):
            if i != len(self.ejemplos[0]) - 1:
                regla += "{}=valor{} Y ".format(atributo, i)
            else:
                regla += "{}=valor{}".format(atributo, i)
        print("Regla FOIL generada:", regla)

# Ejemplo de uso
ejemplos = [
    ['soleado', 'calido', 'normal', 'fuerte', 'calido', 'mismo', True],
    ['soleado', 'calido', 'alto', 'fuerte', 'calido', 'mismo', True],
    ['lluvioso', 'frio', 'alto', 'fuerte', 'calido', 'cambio', False],
    ['soleado', 'calido', 'alto', 'fuerte', 'frio', 'cambio', True]
]

def predicado_objetivo(ejemplo):
    return ejemplo[-1]

foil = FOIL(ejemplos, predicado_objetivo)
foil.foil()
